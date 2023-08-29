FROM python:3.11 as requirements

WORKDIR /tmp

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.11-slim

WORKDIR /api

COPY --from=requirements /tmp/requirements.txt /api/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /api/requirements.txt