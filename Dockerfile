FROM python:3.10.9-slim-buster

ENV PYTHONUNBUFFERED=1 \
  POETRY_VERSION=1.5.1

COPY poetry.lock pyproject.toml /

RUN apt-get update
RUN pip install "poetry==$POETRY_VERSION"
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi

COPY . /src
WORKDIR /src
ARG UID=1000
RUN adduser \
    --disabled-password \
    --no-create-home \
    --shell /bin/bash \
    --gecos "" \
    --uid ${UID} \
    --home /src \
    app
RUN chown -R app:app /src
USER app