FROM python:3.10

### 1. Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

### 2. Setup working dir
RUN mkdir /code
COPY . /code/
WORKDIR /code

### 3. Install dependancies
RUN set -e; \
    /usr/local/bin/python -m pip install --upgrade pip ;\
    python -m pip install --default-timeout=100 -r /code/requirements.txt ;\
    chmod +x /code/docker/entrypoints/entrypoint.sh ;

EXPOSE 8000
ENTRYPOINT ["/code/docker/entrypoints/entrypoint.sh"]