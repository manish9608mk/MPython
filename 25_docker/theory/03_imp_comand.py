'''
============================================================
03 - IMPORTANT DOCKER COMMANDS
============================================================

This file contains important Docker commands
with simple meanings for revision.

============================================================
1. DOCKER VERSION
============================================================

Command:

docker --version

Meaning:

Shows the installed Docker version.

Example:

docker --version


============================================================
2. DOCKER INFO
============================================================

Command:

docker info

Meaning:

Shows information about the Docker Engine,
Docker environment, containers, images, etc.


============================================================
3. DOCKER IMAGES
============================================================

Command:

docker images

Meaning:

Shows all Docker images available locally.

Example output:

IMAGE          TAG       IMAGE ID
ubuntu         latest    513c074113a8
hello-world    latest    5e2309035332


============================================================
4. DOCKER PULL
============================================================

Command:

docker pull ubuntu

Meaning:

Downloads an image from Docker Hub
to your local computer.

Example:

docker pull ubuntu


============================================================
5. DOCKER RUN
============================================================

Command:

docker run ubuntu

Meaning:

Creates a new container from an image
and starts it.

Example:

docker run ubuntu


============================================================
6. DOCKER RUN -IT
============================================================

Command:

docker run -it ubuntu bash

Meaning:

Creates and starts an Ubuntu container
and opens an interactive terminal inside it.

-i  = interactive
-t  = terminal

Example:

docker run -it ubuntu bash

Inside the container:

whoami
pwd
ls
exit


============================================================
7. DOCKER RUN --NAME
============================================================

Command:

docker run -it --name my-ubuntu ubuntu bash

Meaning:

Creates a container with a custom name.

Without --name:

Docker automatically generates a random name.

Example:

my-ubuntu

is easier to remember than:

awesome_jennings


============================================================
8. DOCKER PS
============================================================

Command:

docker ps

Meaning:

Shows currently RUNNING containers.

Important:

docker ps

does NOT show stopped containers.


============================================================
9. DOCKER PS -A
============================================================

Command:

docker ps -a

Meaning:

Shows ALL containers.

This includes:

Running containers
+
Stopped containers


============================================================
10. DOCKER START
============================================================

Command:

docker start my-ubuntu

Meaning:

Starts an existing stopped container.

IMPORTANT:

docker start

does NOT create a new container.

It starts an existing container.


============================================================
11. DOCKER STOP
============================================================

Command:

docker stop my-ubuntu

Meaning:

Stops a running container.

Example:

docker stop my-ubuntu


============================================================
12. DOCKER EXEC
============================================================

Command:

docker exec -it my-ubuntu bash

Meaning:

Opens a new terminal/session inside
an already RUNNING container.

IMPORTANT:

docker exec

requires the container to be running.


============================================================
13. DOCKER RM
============================================================

Command:

docker rm my-ubuntu

Meaning:

Removes a container.

IMPORTANT:

The container normally needs to be stopped first.

Correct:

docker stop my-ubuntu
docker rm my-ubuntu


============================================================
14. FORCE REMOVE CONTAINER
============================================================

Command:

docker rm -f my-ubuntu

Meaning:

Stops and removes the container forcefully.

Use carefully.


============================================================
15. DOCKER RMI
============================================================

Command:

docker rmi ubuntu

Meaning:

Removes a Docker image.

IMPORTANT:

You generally cannot remove an image
while it is still being used by containers.


============================================================
16. DOCKER INSPECT
============================================================

Command:

docker inspect my-ubuntu

Meaning:

Shows detailed information about a container.

For example:

- container configuration
- network
- mounts
- IP information
- environment
- image
- state


============================================================
17. DOCKER LOGS
============================================================

Command:

docker logs my-ubuntu

Meaning:

Shows the output/logs produced by a container.


============================================================
18. DOCKER RUN --DETACH
============================================================

Command:

docker run -d nginx

Meaning:

Runs a container in the background.

-d = detached mode

Example:

docker run -d --name my-nginx nginx


============================================================
19. DOCKER PORT
============================================================

Command:

docker port my-container

Meaning:

Shows the port mappings of a container.


============================================================
20. DOCKER NETWORK LS
============================================================

Command:

docker network ls

Meaning:

Shows Docker networks available on the system.


============================================================
21. DOCKER VOLUME LS
============================================================

Command:

docker volume ls

Meaning:

Shows Docker volumes available on the system.


============================================================
22. DOCKER SYSTEM DF
============================================================

Command:

docker system df

Meaning:

Shows how much disk space Docker is using.

Useful for checking:

Images
Containers
Volumes
Build cache


============================================================
23. DOCKER HELP
============================================================

Command:

docker --help

Meaning:

Shows available Docker commands.

You can also use:

docker run --help

to see options available for docker run.


============================================================
IMPORTANT DIFFERENCE
============================================================

IMAGE
  ↓
Template / blueprint

CONTAINER
  ↓
Running or created instance of an image


Example:

ubuntu IMAGE
     ↓
docker run
     ↓
ubuntu CONTAINER


============================================================
IMPORTANT CONTAINER COMMAND FLOW
============================================================

Create + Start:

docker run -it --name my-ubuntu ubuntu bash

Stop:

docker stop my-ubuntu

Start again:

docker start my-ubuntu

Enter running container:

docker exec -it my-ubuntu bash

Stop:

docker stop my-ubuntu

Remove:

docker rm my-ubuntu


============================================================
MOST IMPORTANT COMMANDS TO REMEMBER
============================================================

docker images
    → list images

docker pull IMAGE
    → download image

docker run IMAGE
    → create + start container

docker ps
    → running containers

docker ps -a
    → all containers

docker start CONTAINER
    → start stopped container

docker stop CONTAINER
    → stop container

docker exec -it CONTAINER bash
    → enter running container

docker logs CONTAINER
    → view logs

docker inspect CONTAINER
    → detailed information

docker rm CONTAINER
    → remove container

docker rmi IMAGE
    → remove image


============================================================
TODAY'S PRACTICE
============================================================

Commands practiced:

docker run -it ubuntu bash
docker ps -a
docker images
docker run -it --name my-ubuntu ubuntu bash
docker start my-ubuntu
docker exec -it my-ubuntu bash
docker rm my-ubuntu


============================================================
REVISION RULE
============================================================

IMAGE = Blueprint

CONTAINER = Instance

docker run = Create + Start

docker start = Start existing container

docker exec = Enter running container

docker stop = Stop container

docker rm = Remove container

docker rmi = Remove image

============================================================
'''