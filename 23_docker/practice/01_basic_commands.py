"""
========================================================
01 - BASIC DOCKER COMMANDS
========================================================

Docker commands used for checking Docker,
images, containers, and basic information.

These are COMMAND NOTES, not Python code.
"""

"""
--------------------------------------------------------
1. CHECK DOCKER VERSION
--------------------------------------------------------

docker --version

Shows the installed Docker version.
"""

"""
--------------------------------------------------------
2. CHECK DOCKER INFORMATION
--------------------------------------------------------

docker info

Shows detailed information about the
Docker Engine.
"""

"""
--------------------------------------------------------
3. CHECK DOCKER HELP
--------------------------------------------------------

docker --help

Shows available Docker commands.
"""

"""
--------------------------------------------------------
4. RUN HELLO WORLD
--------------------------------------------------------

docker run hello-world

Docker will:

1. Check if hello-world image exists locally.
2. If not, download it from Docker Hub.
3. Create a container.
4. Start the container.
5. Run the program.
6. Container exits after the program finishes.
"""

"""
--------------------------------------------------------
5. LIST RUNNING CONTAINERS
--------------------------------------------------------

docker ps

Shows only currently running containers.
"""

"""
--------------------------------------------------------
6. LIST ALL CONTAINERS
--------------------------------------------------------

docker ps -a

Shows:

- Running containers
- Stopped containers
- Exited containers
"""

"""
--------------------------------------------------------
7. LIST IMAGES
--------------------------------------------------------

docker images

Shows images stored locally.
"""

"""
--------------------------------------------------------
8. PULL AN IMAGE
--------------------------------------------------------

docker pull ubuntu

Downloads the Ubuntu image from Docker Hub.
"""

"""
--------------------------------------------------------
9. REMOVE AN IMAGE
--------------------------------------------------------

docker rmi ubuntu

Removes the Ubuntu image.

The image cannot normally be removed if
a container still depends on it.
"""

"""
--------------------------------------------------------
10. DOCKER HUB
--------------------------------------------------------

Docker Hub is a public registry where
Docker images can be stored and downloaded.

Example:

docker pull python
docker pull ubuntu
docker pull nginx
"""