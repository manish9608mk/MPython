"""
========================================================
DOCKER COMPOSE — THEORY
========================================================

1. WHAT IS DOCKER COMPOSE?

Docker Compose is a tool used to run
multiple Docker containers together.

Instead of writing many docker commands manually,
we define everything inside:

    docker-compose.yml

Then we can start the complete application with:

    docker compose up


2. WHY DO WE NEED DOCKER COMPOSE?

Imagine MurphAI has:

    Backend
       ↓
    PostgreSQL
       ↓
    ML Service

Without Compose, we may need several commands:

    docker network create ...
    docker run ...
    docker run ...
    docker run ...

This becomes difficult to manage.

With Docker Compose:

    docker compose up

That's it.


3. WHAT IS docker-compose.yml?

It is a YAML configuration file.

It describes:

    - Services
    - Images
    - Build instructions
    - Ports
    - Networks
    - Volumes
    - Environment variables
    - Dependencies


4. WHAT IS A SERVICE?

A service represents a container/application
that Compose should run.

Example:

    services:

        backend:
            ...

        database:
            ...

Here:

    backend  → one container
    database → another container


5. SIMPLE EXAMPLE

    services:

        web:
            image: nginx

        database:
            image: postgres

Compose will create and manage
both containers.


6. BUILD vs IMAGE

You can either use an existing image:

    image: nginx

OR build your own image:

    build: .

For our Python server:

    server:
        build: .


7. PORTS

Example:

    ports:
        - "8000:8000"

Meaning:

    HOST PORT : CONTAINER PORT

So:

    localhost:8000
          ↓
    container:8000


8. NETWORKING

Compose automatically creates a network
for the services.

Example:

    backend:
        ...

    database:
        ...

The backend can communicate with database
using the service name:

    database

NOT:

    localhost


9. VOLUMES

Volumes allow data to survive
when a container is removed.

Example:

    volumes:
        - db_data:/var/lib/postgresql/data


10. COMMON COMMANDS

Start:

    docker compose up

Start in background:

    docker compose up -d

Stop:

    docker compose down

See containers:

    docker compose ps

See logs:

    docker compose logs

Rebuild:

    docker compose build


11. THE BIG IDEA

Docker:

    "Run this container."

Docker Compose:

    "Run my entire application
     consisting of multiple containers."


12. MURPHAI CONNECTION

Later MurphAI could look like:

    React
       ↓
    FastAPI Backend
       ↓
    PostgreSQL
       ↓
    ML Service

Docker Compose can run
these services together.

========================================================
REMEMBER

docker run
    → usually one container

docker compose
    → multiple related containers

docker-compose.yml
    → configuration of the application
========================================================



The one thing you should remember: 
Don't try to memorize YAML syntax line-by-line.

Remember this mental model:
docker-compose.yml
        ↓
     SERVICES
        ↓
 ┌──────┼────────┐
 ↓      ↓        ↓
Backend Database  ML
 ↓      ↓        ↓
Container Container Container
        ↓
   Docker Network
"""