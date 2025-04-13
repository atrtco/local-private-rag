FROM python:3.10-slim
WORKDIR /usr/src/app
COPY . .
# Install dependencies
RUN pip install -r requirements.txt
# Define environment variables that will be passed to the Docker container
ENV GRADIO_SERVER_NAME="0.0.0.0"
CMD ["python", "app.py"]