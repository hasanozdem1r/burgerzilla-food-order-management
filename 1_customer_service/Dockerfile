# pull official base image
FROM python:3.9.7

# set user
USER root

# set work directory
WORKDIR /customer_service_source

# set environment variables
ENV POSTGRES_HOST="localhost"
ENV POSTGRES_USER="postgres"
ENV POSTGRES_PWD="Hsn58.34"
ENV POSTGRES_PORT="5432"

# update pip and setup poetry
RUN python -m pip install --upgrade pip
RUN pip install poetry

# Install dependencies
ADD ../pyproject.toml ./pyproject.toml
ADD ../poetry.lock ./poetry.lock
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction

ADD ./customer_application ./customer_service_source
RUN poetry install --no-interaction
