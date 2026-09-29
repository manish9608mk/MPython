'''
========================================================
02 — DOCKER ARCHITECTURE
========================================================


1. WHAT IS DOCKER ARCHITECTURE?
--------------------------------------------------------

Docker architecture explains how the different parts of
Docker communicate with each other.

The basic flow is:

    User
      ↓
    Docker CLI
      ↓
    Docker Engine
      ↓
    Container


Docker has several important components:

    • Docker Client / CLI
    • Docker Daemon
    • Docker Engine
    • containerd
    • runc
    • Images
    • Containers
    • Networks
    • Volumes


--------------------------------------------------------
2. HIGH-LEVEL ARCHITECTURE
--------------------------------------------------------

Think of Docker like this:

                USER
                  ↓
             Docker CLI
                  ↓
           Docker Engine
                  ↓
              containerd
                  ↓
                runc
                  ↓
             CONTAINER


You normally interact with Docker through commands such as:

    docker run
    docker build
    docker ps
    docker stop
    docker images


--------------------------------------------------------
3. DOCKER CLI
--------------------------------------------------------

CLI means:

    Command Line Interface


It is the part you interact with from the terminal.

For example:

    docker --version

    docker images

    docker ps

    docker run hello-world


The CLI receives your command and communicates with the
Docker Engine.


Example:

    You type:

        docker run hello-world

    CLI
      ↓
    Docker Engine
      ↓
    Create container
      ↓
    Container runs


Remember:

    Docker CLI = Interface through which we give commands.


--------------------------------------------------------
4. DOCKER DAEMON
--------------------------------------------------------

The Docker daemon is a background service responsible for
managing Docker objects and operations.

It manages things such as:

    • Images
    • Containers
    • Networks
    • Volumes


You can think of it as the worker that actually performs
Docker operations requested through the CLI.


Conceptually:

    Docker CLI
         ↓
    Docker Daemon
         ↓
    Docker Objects


--------------------------------------------------------
5. DOCKER ENGINE
--------------------------------------------------------

Docker Engine is the core technology used to build and
run containers.

It provides the environment required for container
management.

Conceptually:

    Docker CLI
         ↓
    Docker Engine
         ↓
    Containers
    Images
    Networks
    Volumes


When you execute:

    docker run nginx

Docker Engine is responsible for making the required
container run.


--------------------------------------------------------
6. CONTAINERD
--------------------------------------------------------

containerd is a container runtime component used by Docker.

It handles important container lifecycle operations.

For example:

    • Creating containers
    • Starting containers
    • Stopping containers
    • Managing container execution


Simplified architecture:

    Docker Engine
         ↓
      containerd
         ↓
       runc
         ↓
     Container


You usually do not interact directly with containerd
during normal Docker usage.


--------------------------------------------------------
7. RUNC
--------------------------------------------------------

runc is a low-level container runtime.

Its job is to actually create and run containers according
to the OCI container runtime specification.

Simplified:

    Docker
      ↓
    containerd
      ↓
      runc
      ↓
    Container


You normally don't manually use runc.

Docker handles this complexity for you.


--------------------------------------------------------
8. IMAGE
--------------------------------------------------------

Docker images are used as templates for containers.

Example:

    nginx image
         ↓
    docker run
         ↓
    nginx container


Images contain the files and metadata needed to create
a container.


Images are usually downloaded from registries such as:

    Docker Hub
    Amazon ECR
    GitHub Container Registry


--------------------------------------------------------
9. CONTAINER
--------------------------------------------------------

A container is a running or stopped instance created from
a Docker image.

Example:

    Image
      ↓
    docker run
      ↓
    Container


One image can create multiple containers.

Example:

                 nginx image
                /     |     \
               ↓      ↓      ↓
          container container container


Each container can have its own:

    • Process
    • Filesystem layer
    • Network configuration
    • Environment variables


--------------------------------------------------------
10. DOCKER NETWORK
--------------------------------------------------------

Docker provides networking so containers can communicate.

Example:

    FastAPI Container
           ↓
       Docker Network
           ↓
    PostgreSQL Container


This is very important for applications with multiple
services.


Example MurphAI:

    Backend
       ↓
    Network
       ↓
    PostgreSQL


--------------------------------------------------------
11. DOCKER VOLUME
--------------------------------------------------------

Containers have writable storage, but container data can
be lost when the container itself is removed.

Volumes provide persistent storage.

Example:

    PostgreSQL Container
            ↓
         Volume
            ↓
      Database Data


So even if the container is removed, the volume can keep
the data.


--------------------------------------------------------
12. DOCKER REGISTRY
--------------------------------------------------------

A Docker registry stores Docker images.

Example:

    Docker Hub


Basic flow:

    Developer
       ↓
    docker build
       ↓
      Image
       ↓
    docker push
       ↓
    Registry


Another machine:

    Registry
       ↓
    docker pull
       ↓
      Image
       ↓
    docker run
       ↓
    Container


--------------------------------------------------------
13. COMPLETE DOCKER FLOW
--------------------------------------------------------

When you execute:

    docker run hello-world


The simplified flow is:

    You
     ↓
    Docker CLI
     ↓
    Docker Engine
     ↓
    Image lookup
     ↓
    Image pulled if necessary
     ↓
    containerd
     ↓
    runc
     ↓
    Container created
     ↓
    Program executed
     ↓
    Output returned to terminal


This is approximately what happened when we ran:

    docker run hello-world


--------------------------------------------------------
14. DOCKER DESKTOP
--------------------------------------------------------

On macOS and Windows, Docker Desktop provides the Docker
environment in an easy-to-use application.

Your Mac cannot directly run Linux containers using the
same Linux kernel as a native Linux machine.

Docker Desktop therefore provides a Linux environment/VM
under the hood for running Linux containers.

Your setup currently shows:

    Architecture: aarch64

because your Mac uses Apple Silicon.


You normally don't need to manage these internals manually.


--------------------------------------------------------
15. IMPORTANT: CLIENT vs SERVER
--------------------------------------------------------

Docker follows a client-server style architecture.

Client:

    Docker CLI


Server side:

    Docker daemon / Docker Engine


Flow:

    Docker CLI
        ↓
    Docker Engine
        ↓
    Container


This separation allows the client to communicate with
Docker Engine through an API.


--------------------------------------------------------
16. WHY THIS ARCHITECTURE MATTERS
--------------------------------------------------------

You don't need to memorize every internal component.

Understand the responsibility of each:

    Docker CLI
        ↓
    Gives commands


    Docker Engine
        ↓
    Manages Docker operations


    containerd
        ↓
    Manages container lifecycle


    runc
        ↓
    Runs containers


    Container
        ↓
    Runs the application


--------------------------------------------------------
17. EASY REAL-WORLD ANALOGY
--------------------------------------------------------

Imagine a restaurant.

You:

    Customer


Docker CLI:

    Waiter


Docker Engine:

    Restaurant manager


containerd:

    Kitchen coordinator


runc:

    Person actually preparing/starting the order


Container:

    Prepared meal


You don't need to directly manage the kitchen.

You give your request to the waiter.

Similarly:

    You
     ↓
    Docker CLI
     ↓
    Docker Engine
     ↓
    Container


--------------------------------------------------------
18. INTERVIEW QUESTIONS
--------------------------------------------------------

Q1. What is Docker CLI?

Answer:

Docker CLI is the command-line interface used to interact
with Docker.


Q2. What does Docker Engine do?

Answer:

Docker Engine provides the core environment for building,
running and managing containers.


Q3. What is containerd?

Answer:

containerd is a container runtime component responsible
for managing container lifecycle operations.


Q4. What is runc?

Answer:

runc is a low-level OCI-compatible container runtime used
to create and run containers.


Q5. What is Docker Registry?

Answer:

A registry is a service used to store and distribute
Docker images.


Q6. What is Docker Hub?

Answer:

Docker Hub is a public container registry commonly used
to store and download Docker images.


--------------------------------------------------------
19. ONE-MINUTE REVISION
--------------------------------------------------------

Remember this diagram:

                USER
                  ↓
             Docker CLI
                  ↓
           Docker Engine
                  ↓
              containerd
                  ↓
                runc
                  ↓
             CONTAINER
                  ↓
             APPLICATION


And remember:

    CLI
    = gives commands

    Engine
    = manages Docker

    containerd
    = manages container lifecycle

    runc
    = runs the container

    Container
    = runs the application

'''