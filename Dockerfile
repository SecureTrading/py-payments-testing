FROM python:latest

# Get up to date
RUN apt-get update

# Install Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install -y ./google-chrome-stable_current_amd64.deb

# Latest versions of python tools via pip
RUN pip install poetry
COPY pyproject.toml /app/
COPY poetry.lock /app/
WORKDIR /app
RUN poetry install

# Get framework into docker
COPY . /app
RUN chmod 755 /app/chromedriver
ENV PATH "$PATH:/app"
CMD poetry run behave features