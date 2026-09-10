"""
===========================================================
DOCKER NETWORKS — THEORY + COMMANDS
===========================================================

1. WHAT IS A DOCKER NETWORK?
-----------------------------------------------------------

A Docker network allows containers to communicate with:

    Container ↔ Container
    Container ↔ Host
    Container ↔ Internet

Think of a Docker network like a private LAN/network
inside Docker.

Example:

    Backend Container
          |
          | Docker Network
          |
    Database Container


Without networking, containers would not have an easy
way to communicate with each other.


-----------------------------------------------------------

2. WHY DO WE NEED DOCKER NETWORKS?
-----------------------------------------------------------

Imagine a real application:

    React Frontend
          |
          ↓
    FastAPI Backend
          |
          ↓
    PostgreSQL Database

These are often separate containers.

They need to communicate:

    Frontend → Backend
    Backend  → Database

Docker networks allow this communication.


-----------------------------------------------------------

3. SIMPLE REAL-WORLD ANALOGY
-----------------------------------------------------------

Imagine an office.

The office has:

    Computer A
    Computer B
    Computer C

All computers are connected to the same network.

Therefore:

    Computer A → Computer B
    Computer B → Computer C

Docker containers work similarly.

    Container A
    Container B
    Container C

If they are connected to the same Docker network:

    Container A → Container B
    Container B → Container C


-----------------------------------------------------------

4. DEFAULT DOCKER NETWORKS
-----------------------------------------------------------

Docker normally provides some built-in networks.

Check them:

    docker network ls

Typical output:

    NETWORK ID     NAME      DRIVER
    xxxxx          bridge    bridge
    xxxxx          host      host
    xxxxx          none      null

The most important network for beginners is:

    bridge


-----------------------------------------------------------

5. BRIDGE NETWORK
-----------------------------------------------------------

The bridge network is commonly used when containers need
to communicate.

Example:

    Container A
         |
         |
    bridge network
         |
         |
    Container B

Both containers can communicate through the network.


-----------------------------------------------------------

6. CREATE YOUR OWN NETWORK
-----------------------------------------------------------

Command:

    docker network create mynetwork

Check:

    docker network ls

You should see:

    mynetwork


Why create our own network?

Because application containers can be placed inside the
same private network.

Example:

    mynetwork

       ├── backend
       │
       └── database


-----------------------------------------------------------

7. RUN A CONTAINER ON A NETWORK
-----------------------------------------------------------

Command:

    docker run -it \
        --name container1 \
        --network mynetwork \
        alpine \
        sh

Here:

    --network mynetwork

means:

    Connect this container to mynetwork.


-----------------------------------------------------------

8. RUN ANOTHER CONTAINER ON THE SAME NETWORK
-----------------------------------------------------------

Open another terminal.

Run:

    docker run -it \
        --name container2 \
        --network mynetwork \
        alpine \
        sh

Now:

    container1
         |
         |
    mynetwork
         |
         |
    container2

Both containers belong to the same Docker network.


-----------------------------------------------------------

9. CONTAINER-TO-CONTAINER COMMUNICATION
-----------------------------------------------------------

One of the most important Docker concepts:

Containers on the same user-defined network can communicate
using container names.

Example:

    container1
         |
    mynetwork
         |
    container2

From container1, container2 can be addressed by:

    container2

This is much easier than remembering IP addresses.


-----------------------------------------------------------

10. WHY CONTAINER NAMES ARE IMPORTANT
-----------------------------------------------------------

Suppose:

    backend
       |
    mynetwork
       |
    database

Backend needs to connect to PostgreSQL.

Instead of:

    database IP address

we can use:

    database

For example, an application might use:

    DATABASE_HOST=database


This is called Docker's internal DNS/service discovery
behavior.


-----------------------------------------------------------

11. PORT MAPPING vs NETWORKING
-----------------------------------------------------------

IMPORTANT DIFFERENCE:

Docker networking:

    Container ↔ Container

Port mapping:

    Host/Mac ↔ Container

Example:

    docker run -p 8000:8000 backend

means:

    Mac localhost:8000
           ↓
    Container port 8000


It does NOT mean that containers need port mapping to
communicate with each other on the same Docker network.


-----------------------------------------------------------

12. VERY IMPORTANT EXAMPLE
-----------------------------------------------------------

Suppose we have:

    FastAPI Container
          |
          | mynetwork
          |
    PostgreSQL Container


FastAPI connects to PostgreSQL using:

    postgres:5432

NOT:

    localhost:5432


Why?

Because inside the FastAPI container:

    localhost

means:

    FastAPI container itself.


It does NOT mean the PostgreSQL container.


So:

    localhost
        ↓
    current container

while:

    postgres
        ↓
    PostgreSQL container


-----------------------------------------------------------

13. PORT MAPPING EXAMPLE
-----------------------------------------------------------

Suppose FastAPI runs inside:

    Container port: 8000

We want to access it from our Mac.

Use:

    docker run -p 8000:8000 backend

Architecture:

    Browser
       |
       ↓
    localhost:8000
       |
       ↓
    FastAPI Container:8000


-----------------------------------------------------------

14. DATABASE EXAMPLE
-----------------------------------------------------------

Suppose PostgreSQL runs on:

    Container name: postgres

    PostgreSQL port: 5432


FastAPI container:

    backend

Both are connected to:

    mynetwork


Architecture:

    Browser
       |
       ↓
    localhost:8000
       |
       ↓
    FastAPI
       |
       | mynetwork
       ↓
    postgres:5432


This is a very common Docker architecture.


-----------------------------------------------------------

15. INSPECT A NETWORK
-----------------------------------------------------------

Command:

    docker network inspect mynetwork

This shows information about:

    - Network configuration
    - Connected containers
    - IP addresses
    - Driver
    - Subnet
    - Gateway


-----------------------------------------------------------

16. LIST NETWORKS
-----------------------------------------------------------

Command:

    docker network ls


-----------------------------------------------------------

17. CONNECT AN EXISTING CONTAINER
-----------------------------------------------------------

You can connect an existing container to a network.

Command:

    docker network connect mynetwork container1


Now container1 is connected to mynetwork.


-----------------------------------------------------------

18. DISCONNECT A CONTAINER
-----------------------------------------------------------

Command:

    docker network disconnect mynetwork container1


This removes container1 from the network.


-----------------------------------------------------------

19. REMOVE A NETWORK
-----------------------------------------------------------

Command:

    docker network rm mynetwork


IMPORTANT:

You generally cannot remove a network while containers
are still connected to it.

First stop/remove the containers or disconnect them.


-----------------------------------------------------------

20. REMOVE UNUSED NETWORKS
-----------------------------------------------------------

Command:

    docker network prune

This removes unused Docker networks.

Be careful before using prune.


-----------------------------------------------------------

21. MAIN NETWORK COMMANDS
-----------------------------------------------------------

List networks:

    docker network ls


Create:

    docker network create mynetwork


Inspect:

    docker network inspect mynetwork


Connect:

    docker network connect mynetwork container


Disconnect:

    docker network disconnect mynetwork container


Remove:

    docker network rm mynetwork


Remove unused:

    docker network prune


-----------------------------------------------------------

22. COMPLETE PRACTICE FLOW
-----------------------------------------------------------

STEP 1 — Create network

    docker network create mynetwork


STEP 2 — Check network

    docker network ls


STEP 3 — Run first container

    docker run -it \
        --name container1 \
        --network mynetwork \
        alpine \
        sh


STEP 4 — Open another terminal.


STEP 5 — Run second container

    docker run -it \
        --name container2 \
        --network mynetwork \
        alpine \
        sh


STEP 6 — Inspect network

    docker network inspect mynetwork


You should see both:

    container1
    container2

connected to the network.


-----------------------------------------------------------

23. DOCKER NETWORK ARCHITECTURE
-----------------------------------------------------------

                    Docker Host
                         |
             -------------------------
             |                       |
        container1              container2
             |                       |
             -------- mynetwork -------
                       |
                  Communication


-----------------------------------------------------------

24. DOCKER NETWORK + VOLUME
-----------------------------------------------------------

Now combine what you learned.

Volume:

    Container
        |
      Volume
        |
       Data


Network:

    Container
        |
      Network
        |
    Container


Together:

             Docker
                |
       -------------------
       |                 |
    Backend            Database
       |                 |
       -------- network -
                |
             Volume
                |
          Database Data


This is much closer to a real application.


-----------------------------------------------------------

25. MURPHAI CONNECTION
-----------------------------------------------------------

Later, MurphAI can have:

    React Frontend
          |
          ↓
    FastAPI Backend
          |
          ↓
    PostgreSQL
          |
          ↓
    ML Service


Docker can organize these as separate containers.

Example:

    murph-network

        ├── frontend
        │
        ├── backend
        │
        ├── postgres
        │
        └── ml-service


Database data:

    postgres
       |
    postgres_data volume


So:

    Network → Communication

    Volume → Persistent Data

    Container → Application


-----------------------------------------------------------

26. MOST IMPORTANT MEMORY TRICK
-----------------------------------------------------------

Docker Volume:

    "Where is my DATA stored?"

Docker Network:

    "How do my CONTAINERS communicate?"


Remember:

    Volume  = Data
    Network = Communication
    Container = Application


===========================================================
IMPORTANT COMMAND CHEAT SHEET
===========================================================

docker network ls

docker network create mynetwork

docker network inspect mynetwork

docker network connect mynetwork container

docker network disconnect mynetwork container

docker network rm mynetwork

docker network prune


===========================================================
WHAT YOU SHOULD UNDERSTAND BEFORE MOVING ON
===========================================================

You should be able to explain:

1. What is a Docker network?
2. Why do containers need networking?
3. What is a bridge network?
4. Why create a custom network?
5. What does --network do?
6. How do containers communicate?
7. Why can containers use container names?
8. Difference between networking and port mapping.
9. Why localhost is different inside containers.
10. How Docker networks will connect Backend and Database.


===========================================================
ONE-LINE SUMMARY
===========================================================

Docker Network allows containers to communicate with
each other safely and conveniently.

===========================================================
"""