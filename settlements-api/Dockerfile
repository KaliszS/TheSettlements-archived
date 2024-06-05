FROM python:3.11 as build

RUN apt-get update -y
RUN apt-get clean -y
RUN rm -rf /var/lib/apt/lists/*

WORKDIR /tmp

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.11-slim

WORKDIR /api

COPY --from=build /tmp/requirements.txt /api/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /api/requirements.txt
