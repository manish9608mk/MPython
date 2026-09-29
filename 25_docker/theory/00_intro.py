'''
DOCKER — FROM SCRATCH REVISION NOTES

Goal:
I should be able to Dockerize a Python/FastAPI project
from scratch without depending on someone else.


1. DOCKER MENTAL MODEL

Docker solves:

"My application works on my machine, but may not work
on another machine."

Docker packages:

Application Code
+ Dependencies
+ Runtime/Environment
+ Configuration
----------------
= Containerized Application


IMPORTANT:

Dockerfile  = Recipe / Instructions
Image       = Built package / Blueprint
Container   = Running instance of an Image


FLOW:

       Dockerfile
            |
            | docker build
            v
       Docker Image
            |
            | docker run
            v
       Container
            |
            | port mapping
            v
       Your Computer


EASY ANALOGY:

Dockerfile = Cake recipe
Image      = Prepared cake
Container  = Cake served/running



2. CHECK DOCKER

Check Docker installation:

docker --version

Meaning:
Docker is installed and available.


Check running containers:

docker ps

Shows ONLY currently running containers.


Check ALL containers:

docker ps -a

Shows:

Running containers
Stopped containers
Exited containers



3. BASIC PROJECT STRUCTURE

Example Python/FastAPI project:

my-project/
│
├── backend/
│   ├── app.py
│   └── ...
│
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── .env


First make sure the application works WITHOUT Docker.

Example:

uvicorn backend.app:app --reload

Test:

curl http://localhost:8000/

If application works normally:
THEN Dockerize it.



4. requirements.txt

requirements.txt contains Python dependencies.

Example:

fastapi
uvicorn
python-dotenv

Docker will install these packages inside the image.



5. DOCKERFILE

Dockerfile = instructions used to build the Docker image.

Example:

FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "backend.app:app", "--host", "0.0.0.0", "--port", "8000"]


Meaning:

FROM
→ Selects the base image.

Here:
Python 3.12 + slim Linux environment


WORKDIR
→ Sets the working directory inside the container.

After this, commands operate from:

/app


COPY requirements.txt .
→ Copies requirements.txt from your computer
  into the image.


RUN
→ Executes a command while BUILDING the image.

Here:

pip install --no-cache-dir -r requirements.txt

This installs Python dependencies.


COPY . .
→ Copies the rest of your project into /app.


EXPOSE 8000
→ Documents that the application uses port 8000.

IMPORTANT:

EXPOSE does NOT actually publish the port to your Mac.

Port publishing happens using:

-p 8000:8000


CMD
→ Default command executed when the container starts.

Here it starts Uvicorn/FastAPI.



6. DOCKERFILE QUICK MEMORY

FROM
→ Base environment

WORKDIR
→ Where I work

COPY
→ Bring files inside

RUN
→ Execute during image BUILD

EXPOSE
→ Document application port

CMD
→ Start application when container RUNS


Remember:

FROM
  ↓
WORKDIR
  ↓
COPY requirements
  ↓
RUN install dependencies
  ↓
COPY application
  ↓
EXPOSE
  ↓
CMD



7. .dockerignore

.dockerignore tells Docker what NOT to copy into the image.

Example:

.venv
__pycache__
*.pyc
.env
.git
.DS_Store


Why?

Avoid:

unnecessary files
huge build context
local virtual environments
Git metadata
Python cache
secrets


IMPORTANT:

Usually NEVER copy .env into the Docker image.



8. BUILD THE IMAGE

Command:

docker build -t murphai-backend:0.1 .


Breakdown:

docker build
→ Build a Docker image.

-t
→ Give the image a name/tag.

murphai-backend
→ Image name.

:0.1
→ Image version/tag.

.
→ Current directory is the build context.


Think:

Dockerfile + Project Files
            |
            | docker build
            v
    murphai-backend:0.1



9. WHY "." AT THE END?

Example:

docker build -t myapp:1.0 .

"." means:

"Use the CURRENT DIRECTORY as the build context."

Docker can access files from this context during COPY.


Example:

COPY . .

First ".":
Current build context

Second ".":
Current WORKDIR inside image



10. SEE IMAGES

docker images

OR:

docker image ls


Shows downloaded/built Docker images.

Example:

REPOSITORY          TAG       IMAGE ID
murphai-backend     0.1       abc123...



11. RUN A CONTAINER

docker run -d \
  --name murphai-backend \
  --env-file .env \
  -p 8000:8000 \
  murphai-backend:0.1


Breakdown:

docker run
→ Create and start a container from an image.


-d
→ Detached mode.

Application runs in the background.


--name murphai-backend
→ Give the container a human-readable name.


--env-file .env
→ Load environment variables from .env.


-p 8000:8000
→ Map host port 8000 to container port 8000.


murphai-backend:0.1
→ Image used to create the container.



12. PORT MAPPING

-p 8000:8000

Format:

-p HOST_PORT:CONTAINER_PORT


Therefore:

Mac                         Container
8000  ------------------>  8000


Browser:

http://localhost:8000

reaches the application running inside the container.


Example:

-p 5000:8000

means:

Mac port 5000
      ↓
Container port 8000

So access:

http://localhost:5000



13. CHECK RUNNING CONTAINER

docker ps


Example:

CONTAINER ID   IMAGE                 STATUS
abc123         murphai-backend:0.1   Up 10 seconds


"Up" means the container is currently running.



14. TEST THE API

curl http://localhost:8000/


curl sends an HTTP request.

Basically:

"Hey backend, are you alive?"


Expected:

{"message":"MurphAI is running"}


HTTP 200 OK
means request succeeded.



15. CHECK CONTAINER LOGS

docker logs murphai-backend


Shows logs produced by the container.

Useful for:

errors
startup messages
API requests
debugging


Follow logs continuously:

docker logs -f murphai-backend

-f = follow

It keeps showing new logs.

CTRL + C
exits the log view.

Usually this does NOT stop the container.



16. ENTER INSIDE CONTAINER

docker exec -it murphai-backend bash


Breakdown:

docker exec
→ Execute a command inside a running container.

-it
→ Interactive terminal.

bash
→ Open Bash shell.


If bash doesn't exist:

docker exec -it murphai-backend sh


Once inside:

ls
pwd
env


Inspect files/environment.


Exit:

exit



17. STOP CONTAINER

docker stop murphai-backend


Stops the running container.

Container still exists.


Check:

docker ps

It won't appear because it isn't running.


Check:

docker ps -a

It will appear as stopped/exited.



18. START STOPPED CONTAINER

docker start murphai-backend


Starts an existing stopped container.

You DON'T need to create a new container.



19. RESTART CONTAINER

docker restart murphai-backend


Equivalent idea:

Stop
+
Start



20. REMOVE CONTAINER

docker rm murphai-backend


Removes the container.

Usually:

docker stop murphai-backend
docker rm murphai-backend


IMPORTANT:

Removing container != removing image.

The image can still exist.



21. REMOVE IMAGE

docker rmi murphai-backend:0.1


Removes the Docker image.

IMPORTANT:

Image = package / blueprint
Container = instance

Removing container does NOT automatically remove image.



22. COMPLETE BASIC WORKFLOW

STEP 1:
Write application.

STEP 2:
Test application normally.

uvicorn backend.app:app --reload


STEP 3:
Create requirements.txt.

STEP 4:
Create Dockerfile.

STEP 5:
Create .dockerignore.

STEP 6:
Build image.

docker build -t murphai-backend:0.1 .


STEP 7:
Check image.

docker images


STEP 8:
Run container.

docker run -d \
  --name murphai-backend \
  --env-file .env \
  -p 8000:8000 \
  murphai-backend:0.1


STEP 9:
Check container.

docker ps


STEP 10:
Test application.

curl http://localhost:8000/


STEP 11:
Check logs.

docker logs murphai-backend



23. DEVELOPMENT CYCLE

Suppose you modify app.py.

IMPORTANT:

Existing image does NOT automatically get your new code.

Normally:

Change code
   ↓
Build new image
   ↓
Stop old container
   ↓
Remove old container
   ↓
Start new container


Example:

docker build -t murphai-backend:0.2 .

docker stop murphai-backend

docker rm murphai-backend

docker run -d \
  --name murphai-backend \
  --env-file .env \
  -p 8000:8000 \
  murphai-backend:0.2


Test:

curl http://localhost:8000/



24. ENVIRONMENT VARIABLES

.env:

OPENAI_API_KEY=your_key
DATABASE_URL=your_database_url


Don't hard-code secrets in Python.

BAD:

api_key = "my-secret-key"


Better:

import os

api_key = os.getenv("OPENAI_API_KEY")


Docker:

docker run --env-file .env ...


This injects environment variables into the container.


IMPORTANT:

.env
→ Keep locally

.dockerignore
→ Prevent copying it into image

--env-file .env
→ Give variables to container at runtime



25. BUILD vs RUN

VERY IMPORTANT DIFFERENCE:

docker build
    ↓
Creates IMAGE


docker run
    ↓
Creates + starts CONTAINER


Example:

docker build -t myapp:1.0 .

IMAGE CREATED


docker run myapp:1.0

CONTAINER CREATED + STARTED



26. IMAGE vs CONTAINER

IMAGE:

Read-only template/package.


CONTAINER:

Running/created instance of a Docker image.


Example:

Image:

murphai-backend:0.1


Container:

murphai-backend


One image can create multiple containers.



27. MOST IMPORTANT COMMANDS

Docker version:

docker --version


Running containers:

docker ps


All containers:

docker ps -a


Build image:

docker build -t myapp:1.0 .


List images:

docker images


Run:

docker run -d --name mycontainer -p 8000:8000 myapp:1.0


Logs:

docker logs mycontainer


Follow logs:

docker logs -f mycontainer


Enter container:

docker exec -it mycontainer bash


Stop:

docker stop mycontainer


Start:

docker start mycontainer


Restart:

docker restart mycontainer


Remove container:

docker rm mycontainer


Remove image:

docker rmi myapp:1.0



28. QUICK INTERVIEW QUESTIONS

Q1. What is Docker?

Docker is a containerization platform used to package
applications with their dependencies and run them
consistently across environments.


Q2. What is a Docker image?

A Docker image is a packaged, read-only template used
to create containers.


Q3. What is a container?

A container is an isolated running instance of a Docker image.


Q4. Dockerfile vs Image?

Dockerfile = instructions.
Image = result of those instructions.


Q5. Image vs Container?

Image = blueprint/package.
Container = instance created from that image.


Q6. What does -d mean?

Detached/background mode.


Q7. What does -p 8000:8000 mean?

Map host port 8000 to container port 8000.


Q8. What does docker build do?

Builds a Docker image using the Dockerfile and build context.


Q9. What does docker run do?

Creates and starts a container from an image.


Q10. What does docker logs do?

Displays logs generated by a container.



29. COMMON MISTAKES

Mistake 1:

Forgetting the "." in docker build.

Correct:

docker build -t myapp:1.0 .


Mistake 2:

Application listens only on 127.0.0.1 inside container.

For FastAPI/Uvicorn use:

--host 0.0.0.0


Mistake 3:

Forgetting port mapping:

-p 8000:8000


Mistake 4:

Putting secrets inside Dockerfile.

Don't do:

ENV OPENAI_API_KEY=my-secret


Prefer runtime environment variables.


Mistake 5:

Thinking EXPOSE publishes the port.

EXPOSE
= documentation

-p
= actual host/container port mapping


Mistake 6:

Changing source code and expecting running container
to automatically update.

Without a development volume/hot-reload setup,
rebuild/recreate the container.



30. ONE-MINUTE REVISION

Dockerfile
    ↓
docker build
    ↓
Image
    ↓
docker run
    ↓
Container
    ↓
docker ps
    ↓
curl
    ↓
docker logs


If code changes:

Code change
    ↓
docker build
    ↓
new image
    ↓
new/recreated container



31. MURPHAI REAL EXAMPLE

Image:

murphai-backend:0.1


Container:

murphai-backend


Port:

Mac:        8000
Container: 8000


Start:

docker run -d \
  --name murphai-backend \
  --env-file .env \
  -p 8000:8000 \
  murphai-backend:0.1


Check:

docker ps


Test:

curl http://localhost:8000/


Logs:

docker logs murphai-backend


Expected:

Uvicorn running on http://0.0.0.0:8000

GET / 200 OK



32. COMMAND MEMORY TRICK

BUILD

docker build -t NAME:TAG .


RUN

docker run -d --name CONTAINER -p HOST:CONTAINER IMAGE:TAG


SEE

docker ps
docker ps -a
docker images


DEBUG

docker logs CONTAINER
docker exec -it CONTAINER bash


CONTROL

docker stop CONTAINER
docker start CONTAINER
docker restart CONTAINER


DELETE

docker rm CONTAINER
docker rmi IMAGE



33. FINAL MENTAL MODEL

"I write a Dockerfile.

Docker uses it to BUILD an image.

I RUN that image to create a container.

I MAP its port so my computer can access it.

I CHECK it with docker ps.

I TEST it with curl.

I DEBUG it with docker logs.

I STOP/START/REMOVE the container when needed."


CORE FLOW:

Dockerfile
    ↓
BUILD
    ↓
IMAGE
    ↓
RUN
    ↓
CONTAINER
    ↓
TEST
    ↓
LOGS
    ↓
STOP
    ↓
START
    ↓
REMOVE


'''