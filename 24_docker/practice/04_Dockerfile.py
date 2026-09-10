"""
===========================================================
04 - DOCKERFILE
===========================================================

A Dockerfile is a text file containing instructions
used to BUILD a Docker image.

Basic flow:

    Dockerfile
         ↓
    docker build
         ↓
    Docker Image
         ↓
    docker run
         ↓
    Container


-----------------------------------------------------------
1. BASIC DOCKERFILE
-----------------------------------------------------------

Example:

FROM python:3.12-slim

WORKDIR /app

COPY app.py .

RUN pip install --no-cache-dir requests

CMD ["python", "app.py"]


-----------------------------------------------------------
2. IMPORTANT DOCKERFILE INSTRUCTIONS
-----------------------------------------------------------

FROM
    Defines the base image.

    Example:
        FROM python:3.12-slim


WORKDIR
    Sets the working directory inside the container.

    Example:
        WORKDIR /app


COPY
    Copies files from your computer
    into the Docker image.

    Example:
        COPY app.py .


RUN
    Executes a command while BUILDING the image.

    Example:
        RUN pip install requests


CMD
    Defines the default command when
    the container starts.

    Example:
        CMD ["python", "app.py"]


EXPOSE
    Documents which port the application uses.

    Example:
        EXPOSE 8000


ENV
    Defines environment variables.

    Example:
        ENV APP_ENV=production


-----------------------------------------------------------
3. BUILD vs RUN
-----------------------------------------------------------

docker build

    Dockerfile
        ↓
    Image


docker run

    Image
      ↓
    Container


Important:

    RUN  → happens during IMAGE BUILD
    CMD  → happens when CONTAINER STARTS


-----------------------------------------------------------
4. SIMPLE EXAMPLE
-----------------------------------------------------------

Dockerfile:

FROM python:3.12-slim

WORKDIR /app

COPY app.py .

CMD ["python", "app.py"]


Then:

docker build -t my-python-app .

docker run --name my-python-container my-python-app


-----------------------------------------------------------
5. WHY DOCKERFILE MATTERS
-----------------------------------------------------------

Without Dockerfile:

    You manually install
    Python
    dependencies
    configuration
    system packages
    etc.


With Dockerfile:

    Dockerfile
        ↓
    Same environment
        ↓
    Same application
        ↓
    Anywhere Docker runs


This gives us:

    Reproducibility
    Consistency
    Automation
    Easy deployment


-----------------------------------------------------------
6. DOCKERFILE FOR A PYTHON APP
-----------------------------------------------------------

Example application:

app.py

    print("Hello from Docker!")


Dockerfile:

FROM python:3.12-slim

WORKDIR /app

COPY app.py .

CMD ["python", "app.py"]


Build:

docker build -t hello-python .


Run:

docker run --name hello-python-container hello-python


-----------------------------------------------------------
7. COMMON COMMANDS
-----------------------------------------------------------

Build image:

docker build -t image-name .


List images:

docker images


Run container:

docker run image-name


Run with custom name:

docker run --name my-container image-name


List containers:

docker ps


List all containers:

docker ps -a


Remove container:

docker rm my-container


Remove image:

docker rmi image-name


-----------------------------------------------------------
8. .dockerignore
-----------------------------------------------------------

.dockerignore tells Docker which files
should NOT be copied into the image.

Example:

.venv
__pycache__
.git
.env
.pytest_cache
*.db


For a Python project, this is very important.


-----------------------------------------------------------
9. IMPORTANT MENTAL MODEL
-----------------------------------------------------------

Dockerfile
    ↓
docker build
    ↓
IMAGE
    ↓
docker run
    ↓
CONTAINER


Remember:

Dockerfile = Recipe

Image = Prepared food

Container = Running food


A Dockerfile tells Docker HOW to create
the environment.

An image is the packaged result.

A container is a running instance of that image.


"""