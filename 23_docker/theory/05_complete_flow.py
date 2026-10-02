'''
For a Python/FastAPI project like MurphAI, Docker ka complete flow basically ye hai:

Your Code
   ↓
Dockerfile
   ↓
docker build
   ↓
Docker Image
   ↓
docker run
   ↓
Docker Container
   ↓
Test API
   ↓
docker logs
   ↓
docker stop / start / remove


1. First: Check Docker
docker --version

Checks whether Docker is installed.

Then:

docker ps

Shows currently running containers.


2. Create your application
Example:

my-project/
├── backend/
│   └── app.py
├── requirements.txt
├── Dockerfile
└── .env

Your application must work without Docker first.

For example:

uvicorn backend.app:app --reload

Test:

curl http://localhost:8000/

If this works → move to Docker.



3. Create requirements.txt

Example:

fastapi
uvicorn
python-dotenv

This tells Docker:

"These Python packages are required by my application."



4. Create Dockerfile

This is the recipe for creating your Docker image.

Example:

FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "backend.app:app", "--host", "0.0.0.0", "--port", "8000"]

Think:

FROM       → Which base environment?
WORKDIR    → Where will my code live?
COPY       → Bring files inside image
RUN        → Install dependencies
EXPOSE     → Document application port
CMD        → What should start when container runs?


5. Create .dockerignore

Very important.

Example:

.venv
__pycache__
*.pyc
.env
.git
.DS_Store

This tells Docker:

"Don't copy these things into the image."

Especially:

.env

because it can contain secrets.


6. Build the Docker image

From the project root:

docker build -t murphai-backend:0.1 .

Meaning:

docker build       → build an image
-t                 → give it a name/tag
murphai-backend    → image name
:0.1               → version/tag
.                  → use current directory as build context

After this:

docker images

You should see:

murphai-backend    0.1


7. Run the container

Now create a container from that image:

docker run -d \
  --name murphai-backend \
  --env-file .env \
  -p 8000:8000 \
  murphai-backend:0.1

Remember the difference:

Dockerfile
    ↓
Image
    ↓
Container

Image = blueprint

Container = running instance of that blueprint


8. Check whether container is running
docker ps

If you see:

murphai-backend
Up ...

✅ Container is running.

To see all containers, including stopped ones:

docker ps -a


9. Test your application
curl http://localhost:8000/

If you get:

{"message":"MurphAI is running"}

🎉 Your application is running inside Docker.

You can also open:

http://localhost:8000

in your browser.


10. Check logs
docker logs murphai-backend

Useful when something isn't working.

For continuously watching logs:

docker logs -f murphai-backend

Stop watching with:

CTRL + C

This does not necessarily stop the container; it just exits the log view.


11. Check inside the container

Sometimes you need to enter the container.

docker exec -it murphai-backend bash

If bash isn't available:

docker exec -it murphai-backend sh

Now you're inside the container.

For example:

ls

You can inspect your application files.

Exit:

exit


12. Stop the container
docker stop murphai-backend

Container stops.

Check:

docker ps

It won't appear because it's no longer running.

But:

docker ps -a

will show it.


13. Start it again

You don't need to create another container.

Just:

docker start murphai-backend

Then:

docker ps


14. Restart it
docker restart murphai-backend

Useful after certain configuration/application changes.


15. Remove the container

First stop it:

docker stop murphai-backend

Then:

docker rm murphai-backend

Now the container is deleted.

Important: deleting a container does not automatically delete the image.


16. Remove the image
docker rmi murphai-backend:0.1

Now the image is deleted.


17. The most important development cycle

When you change your Python code, remember:

Change code
   ↓
docker build
   ↓
new image
   ↓
remove old container
   ↓
run new container
   ↓
test

For example:

docker build -t murphai-backend:0.2 .

Then:

docker stop murphai-backend
docker rm murphai-backend

Then:

docker run -d \
  --name murphai-backend \
  --env-file .env \
  -p 8000:8000 \
  murphai-backend:0.2

Then:

curl http://localhost:8000/


18. Very important: .env

Suppose your .env contains:

OPENAI_API_KEY=xxxxx
DATABASE_URL=xxxxx

Don't put it inside your Docker image.

Instead:

docker run --env-file .env ...

Docker injects those variables into the container at runtime.

Inside Python:

import os

api_key = os.getenv("OPENAI_API_KEY")


19. Port mapping — understand this properly

This:

-p 8000:8000

means:

Mac                          Container
8000  ───────────────────→   8000

So:

http://localhost:8000

reaches your application inside the container.

If your container application runs on port 8000, you generally use:

-p 8000:8000


20. The commands you should memorize first

Don't try to memorize 50 Docker commands.

Start with these:

docker --version
docker build -t myapp:1.0 .
docker images
docker run -d --name mycontainer -p 8000:8000 myapp:1.0
docker ps
docker ps -a
docker logs mycontainer
docker logs -f mycontainer
docker exec -it mycontainer bash
docker stop mycontainer
docker start mycontainer
docker restart mycontainer
docker rm mycontainer
docker rmi myapp:1.0
🧠 The mental model you should remember

This is the one diagram I want you to understand:

                 YOUR PROJECT
                      │
                      ▼
                Dockerfile
                      │
                docker build
                      │
                      ▼
                 DOCKER IMAGE
               myapp:1.0
                      │
                 docker run
                      │
                      ▼
                CONTAINER
                 mycontainer
                      │
             ┌────────┴────────┐
             │                 │
             ▼                 ▼
          Port 8000          Logs
             │                 │
             ▼                 ▼
       localhost:8000     docker logs

And the lifecycle:

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
For your MurphAI specifically

What you just did was exactly the correct basic Docker workflow:

Dockerfile
   ↓
murphai-backend:0.1
   ↓
docker run
   ↓
murphai-backend container
   ↓
port 8000
   ↓
curl /
   ↓
"MurphAI is running"
   ↓
docker logs
   ↓
Everything OK ✅

'''