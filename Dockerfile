FROM ubuntu:19.10


# python and relevant tools
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    python3 \
    python3-dev \
    python3-pip \
    python3-venv \
    libxml2-dev \
    libxslt-dev \
    libssl-dev \
    zlib1g-dev \
    libyaml-dev \
    libffi-dev \
    firefox \
    xvfb

# Latest versions of python tools via pip
RUN pip3 install --upgrade pip \
                          poetry
COPY pyproject.toml /app/
COPY poetry.lock /app/
WORKDIR /app
RUN poetry install
COPY . /app
CMD poetry run behave tests/e2e/features