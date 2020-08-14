FROM python:latest as payments-tests

# Get up to date
RUN apt-get update

# Install Chrome
RUN wget --quiet https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && apt-get install -qq ./google-chrome-stable_current_amd64.deb

# Make JAVA_HOME available in docker
RUN apt-get install -y openjdk-11-jdk-headless \
    && rm -rf /var/lib/apt/lists/*
ENV JAVA_HOME  /usr/lib/jvm/java-11-openjdk-amd64/

# Latest versions of python tools via pip
RUN pip install poetry
COPY . /app/
WORKDIR /app
RUN python3 -m venv venv \
    && . venv/bin/activate \
    && poetry install

# Install BrowserStack
#RUN wget --quiet https://www.browserstack.com/browserstack-local/BrowserStackLocal-linux-x64.zip \
#    && unzip BrowserStackLocal-linux-x64.zip \
#    && ./BrowserStackLocal <key> --force-local $FORCE_LOCAL --only "domain.com"


# Get framework into docker
ENV PATH "$PATH:/app"
