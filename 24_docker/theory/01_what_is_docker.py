'''
========================================================
01 — WHAT IS DOCKER?
========================================================


1. WHAT IS DOCKER?
------------------

Docker is a platform used to package and run applications
inside isolated environments called CONTAINERS.

A Docker container contains the application and the
dependencies required to run that application.

Example:

    Python Application
          +
    Python Libraries
          +
    Configuration
          +
    Required Files
          ↓
        Docker
          ↓
      Container


The main goal of Docker is to make an application run
consistently across different machines.


--------------------------------------------------------
2. THE PROBLEM BEFORE DOCKER
--------------------------------------------------------

Imagine you build a Python application on your Mac.

Your application needs:

    Python 3.12
    FastAPI
    NumPy
    Pandas
    PostgreSQL
    Some configuration

It works perfectly on your computer.

Now you give the project to another developer.

They may have:

    Python 3.10
    Different library versions
    Different OS
    Missing dependencies
    Different configuration

Your application may fail.

Then they say:

    "It works on my machine."

This is one of the major problems Docker helps solve.


--------------------------------------------------------
3. HOW DOCKER SOLVES THIS
--------------------------------------------------------

Docker packages the application environment together.

Instead of saying:

    "Install Python 3.12"
    "Install these libraries"
    "Configure this"
    "Install that"

we can create a Docker image containing the required
environment.

Then we can run that image as a container.

Conceptually:

    Application
        +
    Dependencies
        +
    Environment
        ↓
      Docker
        ↓
      Image
        ↓
    Container


Now the same containerized application can run on:

    Developer Laptop
          ↓
       Testing
          ↓
       Server
          ↓
        AWS
          ↓
     Production


--------------------------------------------------------
4. WHAT IS A CONTAINER?
--------------------------------------------------------

A container is an isolated environment in which an
application runs.

For example:

    Container
    ┌─────────────────────┐
    │ Python Application  │
    │ Python              │
    │ Libraries           │
    │ Files               │
    │ Configuration       │
    └─────────────────────┘

The application inside the container is isolated from
other applications.


--------------------------------------------------------
5. WHAT IS AN IMAGE?
--------------------------------------------------------

A Docker image is a blueprint/template used to create
containers.

For example:

    Docker Image
          ↓
       docker run
          ↓
      Container


One image can create multiple containers.

Example:

             Python Image
             /    |    \
            ↓     ↓     ↓
       Container Container Container


Remember:

    IMAGE      = Blueprint
    CONTAINER  = Running instance


--------------------------------------------------------
6. DOCKER VS VIRTUAL MACHINE
--------------------------------------------------------

Docker containers and Virtual Machines are different.

Virtual Machine:

    Physical Machine
          ↓
      Host OS
          ↓
      Hypervisor
          ↓
    Virtual Machine
          ↓
     Guest OS
          ↓
     Application


Docker:

    Physical Machine
          ↓
      Host OS
          ↓
    Docker Engine
          ↓
      Container
          ↓
     Application


Containers normally share the host operating system's
kernel, while virtual machines include a complete guest
operating system.

Because of this, containers are generally lighter and
start faster than full virtual machines.


--------------------------------------------------------
7. WHY DO WE USE DOCKER?
--------------------------------------------------------

Main reasons:

1. Consistency

   The application environment can be kept consistent.

2. Isolation

   Applications can run in separate containers.

3. Portability

   The same container image can be used in different
   environments.

4. Fast startup

   Containers usually start much faster than full VMs.

5. Easy deployment

   We can package an application into an image and
   deploy that image elsewhere.

6. Dependency management

   Application dependencies can be included in the
   container environment.

7. Scalability

   Multiple containers can be created when more
   application instances are needed.


--------------------------------------------------------
8. WHEN SHOULD WE USE DOCKER?
--------------------------------------------------------

Docker is useful when:

    • Developing applications
    • Testing applications
    • Running databases locally
    • Building APIs
    • Deploying applications
    • Creating microservices
    • Running ML applications
    • Creating reproducible environments
    • Deploying applications to cloud platforms


For example, MurphAI can eventually use Docker for:

    FastAPI Backend
          ↓
       Container

    PostgreSQL
          ↓
       Container

    ML Service
          ↓
       Container


--------------------------------------------------------
9. BASIC DOCKER FLOW
--------------------------------------------------------

The basic Docker workflow is:

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
    Application


Important commands:

    docker images

    Shows available images.


    docker ps

    Shows running containers.


    docker ps -a

    Shows all containers, including stopped ones.


    docker run <image>

    Creates and starts a container from an image.


--------------------------------------------------------
10. OUR HELLO-WORLD EXAMPLE
--------------------------------------------------------

We already executed:

    docker run hello-world


Docker did approximately this:

    1. Docker checked whether hello-world image existed.

    2. Image was not available locally.

    3. Docker pulled the image from Docker Hub.

    4. Docker created a container from the image.

    5. The container executed its program.

    6. The program printed:
       "Hello from Docker!"

    7. The container finished execution.

That's why:

    docker ps

did not show the container.

But:

    docker ps -a

showed the stopped container.


--------------------------------------------------------
11. IMPORTANT TERMINOLOGY
--------------------------------------------------------

Docker:

    Platform for building, shipping and running
    containerized applications.

Image:

    Blueprint used to create containers.

Container:

    Running instance of an image.

Dockerfile:

    Instructions used to build an image.

Docker Hub:

    Public registry where Docker images can be
    stored and downloaded.

Volume:

    Persistent storage for container data.

Network: 
    Allows containers/services to communicate.


--------------------------------------------------------
12. MOST IMPORTANT DIFFERENCE
--------------------------------------------------------

Remember this:

    Dockerfile
        ↓
      Build
        ↓
      Image
        ↓
       Run
        ↓
    Container


In commands:

    docker build → creates an IMAGE

    docker run   → creates/starts a CONTAINER


--------------------------------------------------------
13. REAL-WORLD ANALOGY
--------------------------------------------------------

Think about a food recipe.

Recipe:

    Ingredients
    Instructions
    Cooking process


The recipe is like a:

    Dockerfile


The prepared food blueprint/package is like:

    Docker Image


The actual prepared food is like:

    Container


So:

    Dockerfile → Image → Container


--------------------------------------------------------
14. DOCKER IN MURPHAI
--------------------------------------------------------

Eventually MurphAI will have several components.

For example:

    MurphAI Backend
          ↓
       FastAPI
          ↓
       Docker


    MurphAI Database
          ↓
      PostgreSQL
          ↓
       Docker


    MurphAI ML
          ↓
     ML inference
          ↓
       Docker


Then Docker Compose can manage these containers together.


--------------------------------------------------------
15. INTERVIEW QUESTIONS
--------------------------------------------------------

Q1. What is Docker?

Answer:

Docker is a platform for building, packaging and running
applications in isolated containers.


Q2. Why is Docker used?

Answer:

Docker provides consistency, portability, isolation and
simplifies application deployment.


Q3. What is a Docker container?

Answer:

A container is an isolated runtime environment created
from a Docker image.


Q4. What is a Docker image?

Answer:

An image is a read-only template used to create containers.


Q5. Docker vs VM?

Answer:

Containers generally share the host kernel and are lighter,
while VMs include a complete guest operating system.


Q6. What is the relationship between image and container?

Answer:

An image is the blueprint and a container is an instance
created from that image.


--------------------------------------------------------
16. ONE-MINUTE REVISION
--------------------------------------------------------

Docker:

    Package + Run applications consistently.


Image:

    Blueprint.


Container:

    Running instance of an image.


Dockerfile:

    Recipe for creating an image.


Docker Build:

    Dockerfile → Image.


Docker Run:

    Image → Container.


Docker Hub:

    Registry for Docker images.


Main benefit:

    "Works the same way across environments."

'''