# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.9

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
        git \
        nginx

# Instalar requirementos
COPY requirements.txt .
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

WORKDIR /app

