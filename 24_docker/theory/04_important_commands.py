"""
===========================================================
DOCKER IMPORTANT COMMANDS — QUICK REVISION
===========================================================

Don't memorize every command.
Understand this pattern:

    docker <object> <action> <options>

Common objects:
    image
    container
    volume
    network

===========================================================
1. BASIC DOCKER
===========================================================

Check Docker version:

    docker --version

Check Docker installation and engine:

    docker info

Test Docker:

    docker run hello-world


===========================================================
2. IMAGES
===========================================================

List images:

    docker images

Download an image:

    docker pull ubuntu

Remove an image:

    docker rmi ubuntu

Build an image:

    docker build -t my-image .

Run an image:

    docker run my-image


===========================================================
3. CONTAINERS
===========================================================

Run a container:

    docker run ubuntu

Run interactively:

    docker run -it ubuntu bash

Run in background:

    docker run -d ubuntu

Give container a name:

    docker run --name my-container ubuntu

Automatically remove container after stopping:

    docker run --rm ubuntu

List RUNNING containers:

    docker ps

List ALL containers:

    docker ps -a

Stop container:

    docker stop my-container

Start stopped container:

    docker start my-container

Restart container:

    docker restart my-container

Remove container:

    docker rm my-container

Force remove running container:

    docker rm -f my-container

Execute command inside running container:

    docker exec -it my-container bash

View container logs:

    docker logs my-container

Inspect container:

    docker inspect my-container


===========================================================
4. PORTS
===========================================================

Publish container port to host:

    docker run -p 8000:8000 my-image

Meaning:

    Host:8000
        ↓
    Container:8000

Example:

    docker run --rm -p 8000:8000 fastapi-ports

Then open:

    http://localhost:8000


===========================================================
5. VOLUMES
===========================================================

Create volume:

    docker volume create mydata

List volumes:

    docker volume ls

Inspect volume:

    docker volume inspect mydata

Delete volume:

    docker volume rm mydata

Mount volume into container:

    docker run -it \
        -v mydata:/data \
        alpine sh

Meaning:

    mydata  →  /data

Host/Docker managed storage
        ↓
    Container


===========================================================
6. NETWORKS
===========================================================

List networks:

    docker network ls

Create network:

    docker network create mynetwork

Inspect network:

    docker network inspect mynetwork

Remove network:

    docker network rm mynetwork

Run container inside a network:

    docker run -d \
        --name server-container \
        --network mynetwork \
        network-server

Run client inside same network:

    docker run -it --rm \
        --name client-container \
        --network mynetwork \
        alpine sh

Test communication:

    wget -qO- http://server-container:8000


===========================================================
7. NETWORK MENTAL MODEL
===========================================================

Two containers:

    server-container
          │
          │
      mynetwork
          │
          │
    client-container

Inside Docker network:

    http://server-container:8000

Container name can be used as hostname.

You don't normally need to remember the container IP.


===========================================================
8. DOCKERFILE
===========================================================

Build image:

    docker build -t my-image .

Important:

    Dockerfile
        ↓
    docker build
        ↓
    Image
        ↓
    docker run
        ↓
    Container


===========================================================
9. MOST IMPORTANT COMMANDS
===========================================================

If you forget everything, remember these first:

    docker images

    docker ps

    docker ps -a

    docker run

    docker stop

    docker start

    docker exec

    docker logs

    docker rm

    docker rmi

    docker build

    docker pull

    docker volume ls

    docker network ls


===========================================================
10. SIMPLE COMMAND FLOW
===========================================================

IMAGE:

    pull
      ↓
    build
      ↓
    image
      ↓
    run
      ↓
    container

CONTAINER:

    run
      ↓
    ps
      ↓
    exec / logs
      ↓
    stop
      ↓
    start
      ↓
    rm

VOLUME:

    create
      ↓
    mount
      ↓
    use
      ↓
    remove

NETWORK:

    create
      ↓
    connect containers
      ↓
    communicate
      ↓
    inspect
      ↓
    remove


===========================================================
11. GOLDEN RULE
===========================================================

Don't memorize commands word-by-word.

Think:

    What am I working with?
        ↓
    Image?
    Container?
    Volume?
    Network?

Then:

    What do I want to do?
        ↓
    create?
    list?
    inspect?
    start?
    stop?
    remove?
    run?

Example:

"I want to see networks"

    docker network ls

"I want to inspect a network"

    docker network inspect mynetwork

"I want to create a network"

    docker network create mynetwork

"I want to run a container in that network"

    docker run --network mynetwork ...


===========================================================
12. INTERVIEW MEMORY
===========================================================

IMAGE = Blueprint

CONTAINER = Running instance of image

VOLUME = Persistent storage

NETWORK = Communication between containers

PORT = Connection between host and container

Dockerfile = Instructions for building an image

docker build = Build image

docker run = Create + start container


===========================================================

And one important thing: 
Don't worry if you forget -it, -d, --rm, -p, -v, --network.
You'll naturally remember them because we're going to use them repeatedly in actual scenarios.

For example:
Need terminal inside container
        ↓
-it

Need background service
        ↓
-d

Need temporary container
        ↓
--rm

Need host ↔ container connection
        ↓
-p

Need persistent storage
        ↓
-v

Need container ↔ container communication
        ↓
--network
"""