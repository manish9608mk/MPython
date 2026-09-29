'''
$ docker build -t network-server .

[+] Building 2.7s (9/9) FINISHED
✔ Dockerfile loaded
✔ Python 3.12-slim image pulled
✔ Build context transferred
✔ server.py copied
✔ Image built successfully

Successfully tagged network-server:latest


$ docker images

IMAGE                  ID             SIZE
network-server:latest  bb5c9cb08913   214MB
alpine:latest          28bd5fe8b56d   13.6MB
ubuntu:latest          513c074113a8   180MB


$ docker network create mynetwork

64cfccdce047648598ccf8b6076a6e050ec3584f49d9e9077252a7f17136c6c8


$ docker network ls

NETWORK ID     NAME        DRIVER    SCOPE
02052f174a91   bridge      bridge    local
d449b2286246   host        host      local
64cfccdce047   mynetwork   bridge    local
2712e2d8475a   none        null      local


$ docker run -d \
    --name server-container \
    --network mynetwork \
    network-server

d9cf75d50f4e48b51db17eaaeb805c1c56118fb592e0d55a4dfe7f426a51dcc2


$ docker ps

CONTAINER ID   IMAGE            STATUS        PORTS      NAMES
d9cf75d50f4e   network-server   Up            8000/tcp   server-container


$ docker network inspect mynetwork

Network: mynetwork
Driver: bridge

Server Container:
    Name:        server-container
    IPv4:        172.18.0.2/16


$ docker run -it --rm \
    --name client-container \
    --network mynetwork \
    alpine sh

/ # wget -qO- http://server-container:8000

Hello from Docker Server!

/ # exit


$ docker run -it --rm \
    --name isolated-client \
    alpine sh

/ # wget -qO- http://server-container:8000

wget: bad address 'server-container:8000'

/ # exit


============================================================
DOCKER NETWORKING RESULT
============================================================

mynetwork
    │
    ├── server-container
    │       └── 172.18.0.2:8000
    │
    └── client-container
            │
            └── HTTP request
                    │
                    ▼
            server-container:8000
                    │
                    ▼
          Hello from Docker Server!

                    ✅ SUCCESS


isolated-client
        │
        │  NOT CONNECTED TO mynetwork
        │
        ▼
server-container:8000
        │
        ▼
❌ wget: bad address 'server-container:8000'


============================================================
WHAT WE LEARNED
============================================================

✅ Created a custom Docker bridge network
✅ Connected containers to the same network
✅ Docker assigned server-container IP: 172.18.0.2
✅ Docker provides container-name DNS
✅ Same-network containers can communicate
✅ Used server-container instead of hardcoded IP
✅ Different-network containers cannot resolve the container
✅ Demonstrated Docker container-to-container communication



or,

abhi tumne networking mein ye kiya:
docker network create mynetwork
docker network ls
docker network inspect mynetwork
docker run -d --name server-container --network mynetwork network-server
docker run -it --rm --name client-container --network mynetwork alpine sh
wget -qO- http://server-container:8000

Inko individually memorize mat karo. Mental model yaad rakho:
Docker
  │
  ├── Image
  │     └── docker images
  │
  ├── Container
  │     ├── docker run
  │     ├── docker ps
  │     ├── docker stop
  │     ├── docker start
  │     ├── docker exec
  │     └── docker rm
  │
  ├── Volume
  │     ├── docker volume create
  │     ├── docker volume ls
  │     └── docker volume inspect
  │
  └── Network
        ├── docker network create
        ├── docker network ls
        ├── docker network inspect
        └── docker run --network


        
The golden rule - 

Most Docker commands follow:

docker
   ↓
WHAT
   ↓
ACTION
   ↓
OPTIONS

For example:

docker network create mynetwork

means:

Docker → network → create → mynetwork

Similarly:

docker volume create mydata

means:

Docker → volume → create → mydata

And:

docker network inspect mynetwork

means:

Docker → network → inspect → mynetwork
'''