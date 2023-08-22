FROM ubuntu:20.04

RUN apt-get update \
    && apt-get -y install tesseract-ocr \
    && apt-get install -y python3 python3-distutils python3-pip \
    && cd /usr/local/bin \
    && ln -s /usr/bin/python3 python \
    && pip3 --no-cache-dir install --upgrade pip

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

ARG POETRY_VERSION=1.7.0
RUN pip install 'poetry==$POETRY_VERSION'
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi

COPY . /app/

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
