<a id="readme-top"></a>

<!-- INTRO -->
<br />
<div align="center">
  <h1 align="center">Local Private RAG</h1>

  <p align="center">
    Easily host a secure assistant chatbot to answer questions based on your private documents!
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project

This project allows users to host a private chatbot platform locally and securely. It aims to self-host intelligent assistants who can answer questions based on a library of uploaded documents with the help of AI and LLM technologies.

### Built With

[![Python][python-shield]][python-url] [![Langchain][langchain-shield]][langchain-url] [![Ollama][ollama-shield]][ollama-url] [![Gradio][gradio-shield]][gradio-url] [![Docker][docker-shield]][docker-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To use this private chatbot script, please refer to the instructions below.

### Requirements

- Docker (recommended) or Python 3.10 installed
- Ollama installed and running
- .env file containing project variables
- pdf files

### Setup

1. Install [Docker](https://www.docker.com/). (recommended)
<br/>_To check if Docker is installed correctly, run the following command in the terminal. The installed version should be returned._
   ```sh
   docker --version
   ```
   
   You may also use Python instead of Docker. To proceed with this option, install [Python](https://www.python.org/) and the specified packages under `requirements.txt`. It is recommended to create a new python environment for this specific project. 

2. Install [Ollama](https://www.ollama.com/).
<br/>_To check if Ollama is installed correctly, run the following command in the terminal. The installed version should be returned._
   ```sh
   ollama --version
   ```

3. Identify the URL and port where Ollama is hosted.
<br/>_Normally, Ollama is hosted at http://127.0.0.1:11434/_
<br/>_But if you will be deploying this chatbot via Docker, you need to identify the IP address of your system. The URL should be in this format: http://x.x.x.x:11434/_
<br/>_To check if the Ollama URL is correct, visit that URL using your web browser and you should see the text "Ollama is running." on your browser._

4. Pull two LLM models from Ollama via the terminal/command prompt. Replace (model-name) with the name of your preferred model.
- Embedding model options: nomic-embed-text, mxbai-embed-large, or any embedding model listed in [Ollama](https://www.ollama.com/)
   ```sh
   ollama pull (model-name)
   ```
- LLM model options: gemma3, llama3.3, phi4, mistral, deepseek-v3, or any model listed in [Ollama](https://www.ollama.com/)
   ```sh
   ollama pull (model-name)
   ```

5. Clone this GitHub repo and open terminal in this directory.
   ```sh
   git clone https://github.com/atrtco/local-private-rag.git
   ```

6. Prepare your pdf files.
Two possible approaches:
- Recommended for Docker and Python deployment: Save the pdf files under the 'pdfs' folder of this project. 
- Alternative (applicable for Docker deployment only): Mount the folder of the pdfs when runnnig docker-compose. Update the specified volume in the `docker-compose.yaml` file.

7. Update the `.env` file, if necessary. Below is the description of each variable used.
- TOPIC = Topic to be displayed in the Web App
- WEB_TITLE = Web App Title
- OLLAMA_BASE_URL = Ollama URL based on Step#3.
- EMBEDDING_MODEL_NAME = Embedding model used to load the pdf documents. This should match with the model downloaded from Step#4.
- LLM_MODEL_NAME = LLM model used by the chatbot. This should match with the model downloaded from Step#4.
- CHUNK_SIZE = Text splitting chunk size parameter
- CHUNK_OVERLAP = Text splitting chunk overlap parameter
- MAIN_PROMPT = Instructions for the chatbot on how to respond. 

4. Run the script
Two possible approaches:
- Docker deployment
   ```sh
   docker-compose up -d --build
   ```
- Python deployment
   ```python
   python app.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

Once the script is running, you can go to the displayed URL from the terminal using your web browser.
- Default url: http://127.0.0.1:7860

You can now ask your private chatbot about the uploaded documents.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions to this repository are **greatly appreciated**.

<!-- PROJECT -->
## Project

Link: [https://github.com/atrtco/local-private-rag](https://github.com/atrtco/local-private-rag)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[python-shield]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[python-url]: https://www.python.org/
[langchain-shield]: https://img.shields.io/badge/LangChain-ffffff?logo=langchain&logoColor=green
[langchain-url]: https://www.langchain.com/
[ollama-shield]: https://img.shields.io/badge/-Ollama-000000?style=flat&logo=ollama&logoColor=white
[ollama-url]: https://ollama.com/
[gradio-shield]: https://img.shields.io/badge/-Gradio-3E8EFB?style=flat&logo=gradio&logoColor=white
[gradio-url]: https://www.gradio.app/
[docker-shield]: https://img.shields.io/badge/docker-257bd6?style=for-the-badge&logo=docker&logoColor=white
[docker-url]: https://www.docker.com/