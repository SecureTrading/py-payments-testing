#####
# NOTE!
# This is legacy file to keep working travis and docker-compose while migration phase
# New version is located under docker/payments-tests/Dockerfile
#####
FROM python:latest

# Get up to date
RUN apt-get update

# Install Chrome
RUN wget --quiet https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install -qq ./google-chrome-stable_current_amd64.deb

# Make JAVA_HOME available in docker
RUN apt-get install -y openjdk-11-jdk-headless && \
    rm -rf /var/lib/apt/lists/*
ENV JAVA_HOME  /usr/lib/jvm/java-11-openjdk-amd64/

# Latest versions of python tools via pip
RUN pip install poetry
COPY pyproject.toml /app/
COPY poetry.lock /app/
WORKDIR /app
RUN poetry install

# Get framework into docker
ENV PATH "$PATH:/app"
