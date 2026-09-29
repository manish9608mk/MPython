"""
========================================================
03 - CONTAINER LIFECYCLE
========================================================

A Docker container has a lifecycle:

CREATE
  ↓
START
  ↓
RUNNING
  ↓
STOP
  ↓
EXITED
  ↓
START again
  ↓
RUNNING
  ↓
REMOVE
"""


"""
========================================================
1. CREATE + START
========================================================

docker run -it --name my-ubuntu ubuntu bash

This creates AND starts the container.
"""


"""
========================================================
2. CHECK CONTAINER
========================================================

docker ps

Shows running containers.
"""


"""
========================================================
3. CHECK ALL CONTAINERS
========================================================

docker ps -a

Shows running + stopped containers.
"""


"""
========================================================
4. STOP CONTAINER
========================================================

docker stop my-ubuntu

Stops a running container.

The container is NOT deleted.

It still exists.
"""


"""
========================================================
5. START CONTAINER AGAIN
========================================================

docker start my-ubuntu

Starts an existing stopped container.
"""


"""
========================================================
6. ENTER RUNNING CONTAINER
========================================================

docker exec -it my-ubuntu bash

Opens a Bash shell inside
an already-running container.
"""


"""
========================================================
7. EXIT CONTAINER
========================================================

exit

Leaves the shell.

If Bash is the main process of the container,
the container may stop after exit.
"""


"""
========================================================
8. REMOVE CONTAINER
========================================================

docker rm my-ubuntu

Deletes the stopped container.

IMPORTANT:

stop ≠ remove

docker stop
    ↓
container still exists

docker rm
    ↓
container deleted
"""


"""
========================================================
9. FORCE REMOVE
========================================================

docker rm -f my-ubuntu

Stops and removes the container.

Use carefully.
"""


"""
========================================================
COMPLETE LIFECYCLE
========================================================

docker run
     ↓
 CREATED + STARTED
     ↓
 RUNNING
     ↓
docker stop
     ↓
 STOPPED
     ↓
docker start
     ↓
 RUNNING
     ↓
docker stop
     ↓
 STOPPED
     ↓
docker rm
     ↓
 DELETED
"""


"""
========================================================
COMMAND CHEAT SHEET
========================================================

docker ps
    → running containers

docker ps -a
    → all containers

docker start NAME
    → start stopped container

docker stop NAME
    → stop running container

docker exec -it NAME bash
    → enter running container

docker rm NAME
    → remove stopped container

docker rm -f NAME
    → force remove container

docker images
    → list images

docker pull IMAGE
    → download image

docker rmi IMAGE
    → remove image





docker run
    = CREATE + START a NEW container

docker start
    = START an EXISTING container

docker exec
    = ENTER an EXISTING RUNNING container

docker stop
    = STOP container

docker rm
    = DELETE container

docker rmi
    = DELETE image
"""