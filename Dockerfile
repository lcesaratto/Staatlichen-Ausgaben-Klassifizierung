FROM jupyter/datascience-notebook:latest as requirements-stage

WORKDIR /tmp

RUN pip install --no-cache-dir poetry==1.1.12

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM jupyter/datascience-notebook:latest

WORKDIR /code

COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code/

CMD ["jupyter-lab"]