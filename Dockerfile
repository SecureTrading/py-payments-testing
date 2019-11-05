FROM python:latest

# relevant testing tools
RUN apt-get update
RUN apt-get install -y firefox-esr xvfb

# Latest versions of python tools via pip
RUN pip3 install poetry
COPY pyproject.toml /app/
COPY poetry.lock /app/
WORKDIR /app
RUN poetry install

# Get framework into docker
COPY . /app
RUN chmod 755 /app/geckodriver
CMD poetry run behave tests/e2e/features