FROM ubuntu:23.10

RUN apt-get update \
    && apt-get -y install tesseract-ocr \
    && apt-get install -y python3 python3-distutils python3-pip \
    && cd /usr/local/bin \
    && ln -s /usr/bin/python3 python

RUN pip install --upgrade pip --break-system-packages

WORKDIR /app

ARG POETRY_VERSION=1.5.1
RUN pip install "poetry==$POETRY_VERSION" --break-system-packages
RUN poetry config virtualenvs.create false

COPY poetry.lock pyproject.toml /app/
RUN poetry install --no-interaction --no-ansi

COPY . /app/


CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
