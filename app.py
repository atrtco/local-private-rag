# Import packages
### env
from dotenv import load_dotenv
import os
### Langchain
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_ollama.llms import OllamaLLM
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
### Gradio
import gradio as gr



# Define a class for the RAG Chat Bot
class RagChatBot:
    def __init__(self, topic, web_title,
                 ollama_base_url, embedding_model_name,
                 llm_model_name, chunk_size, chunk_overlap,
                 main_prompt):

        self.topic = topic
        self.web_title = web_title
        self.ollama_base_url = ollama_base_url
        self.embedding_model_name = embedding_model_name
        self.llm_model_name = llm_model_name
        self.chunk_size = int(chunk_size)
        self.chunk_overlap = int(chunk_overlap)
        self.main_prompt = main_prompt

    # Load the PDFs saved in 'pdfs' folder
    def load_pdfs(self):
        loader = PyPDFDirectoryLoader(path="./pdfs/", glob="*.pdf", silent_errors=True, load_hidden=False)
        docs = loader.load()
        self.docs = docs
        return (f"{len(docs)} pages from PDF files successfully loaded.")

    # Split documents into chunks
    def split_documents(self):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=self.chunk_size, chunk_overlap=self.chunk_overlap)
        splits = text_splitter.split_documents(self.docs)
        self.splits = splits
        return (f"Loaded data successfully splitted into {len(splits)} chunks.")

    # Initiate the embedding model
    def initiate_embedding_model(self):
        embedder = OllamaEmbeddings(model=self.embedding_model_name, base_url=self.ollama_base_url)
        self.embedder = embedder
        return (f"Ollama {self.embedding_model_name} embedding model initiated.")

    # Create the vector store and fill it with embeddings
    def create_vector_store(self):
        vectorstore = Chroma.from_documents(documents=self.splits, embedding=self.embedder)
        retriever = vectorstore.as_retriever()
        self.retriever = retriever
        return (f"Retriever successfully loaded from Chroma vector store.")

    # Define the llm
    def define_llm(self):
        llm = OllamaLLM(model=self.llm_model_name, base_url=self.ollama_base_url)
        self.llm = llm
        return (f"Ollama {self.llm_model_name} LLM model initiated.")

    # Define the prompt
    def define_prompt(self):
        system_prompt = (
            f"{self.main_prompt}\n\n"
             "{context}"
            )
        
        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt),
                ("human", "{input}"),
            ]
        )
        self.prompt = prompt

    # Create the retrieval chain
    def create_retrieval_chain(self):
        question_answer_chain = create_stuff_documents_chain(self.llm, self.prompt)
        rag_chain = create_retrieval_chain(self.retriever, question_answer_chain)
        self.rag_chain = rag_chain

    def run(self):
        self.initiate_embedding_model()
        self.define_llm()
        self.load_pdfs()
        self.split_documents()
        self.create_vector_store()
        self.define_prompt()
        self.create_retrieval_chain()

# Define a function to respond to questions
class RespondFunction:
    def __init__(self, rag_chain):
        self.rag_chain = rag_chain

    # Define the response function
    def respond(self, question, history):
        result = self.rag_chain.invoke({"input": question})
        return result["answer"]

# Create a Gradio app with the response function
def create_app(bot):
    def respond(question, history):
        bot.run()
        return RespondFunction(bot.rag_chain).respond(question, history)

    app = gr.ChatInterface(
        fn=respond,
        chatbot=gr.Chatbot(type="messages",height=500),
        textbox=gr.Textbox(placeholder=f"Ask me question about {bot.topic}", container=False, scale=7),
        title=bot.web_title
        )
    
    return app

if __name__ == "__main__":
    print("\nInitiating RAG Chatbot...")
    load_dotenv()
    print(os.environ)
    print(f"\n{os.environ['TOPIC']} RAG Chatbot")
    bot = RagChatBot(topic=os.environ['TOPIC'], web_title=os.environ['WEB_TITLE'],
                 ollama_base_url=os.environ['OLLAMA_BASE_URL'], embedding_model_name=os.environ['EMBEDDING_MODEL_NAME'],
                 llm_model_name=os.environ['LLM_MODEL_NAME'], chunk_size=os.environ['CHUNK_SIZE'], chunk_overlap=os.environ['CHUNK_OVERLAP'],
                 main_prompt=os.environ['MAIN_PROMPT'])
    app = create_app(bot)
    app.launch()
