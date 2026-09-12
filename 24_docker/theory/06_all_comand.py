'''
MURPHAI DOCKERIZATION — COMPLETE COMMAND RECALL SHEET

This document contains the Docker commands and workflow used while
containerizing MurphAI.

The goal is NOT to memorize random commands.

The goal is to understand the workflow:

    Build
      ↓
    Run
      ↓
    Check
      ↓
    Debug
      ↓
    Optimize
      ↓
    Verify
      ↓
    Git commit/push


============================================================
1. BASIC DOCKER IMAGE CHECK
============================================================

COMMAND:

docker images

WHAT IT DOES:

Shows Docker images available locally.

Example:

REPOSITORY          TAG       IMAGE ID       SIZE
murphai-backend     latest    xxxxx          1.1GB

IMPORTANT:

Docker Desktop may display a different size representation from
the exact image size returned by `docker image inspect`.

For controlled measurements, prefer:

docker image inspect ...


============================================================
2. GET EXACT IMAGE SIZE
============================================================

COMMAND:

docker image inspect murphai-backend:latest --format '{{.Size}}'

WHAT IT DOES:

Returns the image size in bytes.

We used this to establish a baseline before optimization.

Our baseline:

297934707 bytes

Approximately:

297.9 MB


REAL-WORLD USE:

Whenever you optimize a Docker image:

    BEFORE
       ↓
    make one change
       ↓
    rebuild
       ↓
    AFTER

Never claim that an optimization worked without measuring it.


============================================================
3. CHECK DOCKER COMPOSE CONFIGURATION
============================================================

COMMAND:

docker compose config

WHAT IT DOES:

Validates and renders the final Docker Compose configuration.

It combines things such as:

    docker-compose.yml
    environment variables
    service configuration
    volumes
    ports
    build configuration

Useful for detecting:

    - invalid YAML
    - wrong indentation
    - incorrect service configuration
    - incorrect volume definitions
    - environment expansion problems

IMPORTANT:

`docker compose config` can display environment values.

Therefore:

    NEVER paste secrets from its output into GitHub.

Also make sure `.env` is in `.gitignore`.


============================================================
4. STOP COMPOSE SERVICES
============================================================

COMMAND:

docker compose down

WHAT IT DOES:

Stops and removes containers created by Docker Compose.

It does NOT normally delete named volumes unless explicitly requested.

Typical workflow:

docker compose down

Then rebuild/restart:

docker compose up --build -d


REAL-WORLD USE:

Use this when you want a clean restart of your Compose application.


============================================================
5. BUILD + START THE APPLICATION
============================================================

COMMAND:

docker compose up --build -d

BREAKDOWN:

docker compose
    → use Docker Compose

up
    → create/start services

--build
    → rebuild the image if necessary

-d
    → detached mode
       terminal remains usable

Typical real-world workflow:

docker compose up --build -d


============================================================
6. START WITHOUT REBUILDING
============================================================

COMMAND:

docker compose up -d

WHAT IT DOES:

Starts the existing Compose image/container configuration.

Use this when:

    - image already exists
    - Dockerfile did not change
    - you simply stopped the container
    - you want to restart the application

Difference:

docker compose up -d

    → use existing image when possible


docker compose up --build -d

    → build image first, then start


============================================================
7. CHECK RUNNING CONTAINERS
============================================================

COMMAND:

docker compose ps

WHAT IT DOES:

Shows the services managed by the current Compose project.

Example:

NAME              SERVICE   STATUS
murphai-backend   backend   Up (healthy)

IMPORTANT:

`healthy` means the Docker HEALTHCHECK is passing.

For MurphAI we verified:

    Up ... (healthy)

and:

    0.0.0.0:8000->8000/tcp


============================================================
8. CHECK ALL DOCKER CONTAINERS
============================================================

COMMAND:

docker ps

Shows currently running containers.

For stopped containers:

docker ps -a


Difference:

docker ps

    → running containers

docker ps -a

    → running + stopped containers


============================================================
9. VIEW CONTAINER LOGS
============================================================

COMMAND:

docker compose logs backend

WHAT IT DOES:

Shows logs produced by the backend service.

For live/following logs:

docker compose logs -f backend

`-f` means follow.

Useful when:

    - API doesn't start
    - Uvicorn crashes
    - import error occurs
    - database connection fails
    - application returns 500
    - container becomes unhealthy


============================================================
10. ENTER A RUNNING CONTAINER
============================================================

COMMAND:

docker compose exec backend bash

WHAT IT DOES:

Opens a shell inside the running backend container.

You can then run:

whoami

python --version

pip list

ls

pwd

etc.

If bash is unavailable:

docker compose exec backend sh


REAL-WORLD IMPORTANCE:

This is one of the most useful Docker debugging techniques.

You are effectively inspecting:

    "What actually exists inside my container?"


============================================================
11. RUN A SINGLE COMMAND INSIDE CONTAINER
============================================================

Instead of opening a shell:

docker compose exec backend whoami

We used:

docker compose exec backend whoami

Result:

murphai

This verified that the application was NOT running as root.


============================================================
12. WHY NON-ROOT USERS MATTER
============================================================

Inside a container:

root
    ↓
has very high privileges

Application user
    ↓
has limited privileges

Production containers should generally avoid running
the application as root.

Our Dockerfile creates:

USER murphai

Then Uvicorn runs as:

murphai


VERIFY:

docker compose exec backend whoami


Expected:

murphai


============================================================
13. TEST PYTHON RUNTIME INSIDE CONTAINER
============================================================

COMMAND:

docker compose exec backend python --version

Useful for checking:

    - Python version
    - whether Python exists
    - whether correct base image is being used


============================================================
14. TEST INSTALLED PACKAGES
============================================================

COMMAND:

docker compose exec backend python -m pip list

Shows packages installed inside the container.

Useful when debugging:

    ModuleNotFoundError
    dependency conflicts
    incorrect package versions


Specific package:

docker compose exec backend python -m pip show mlflow

Another example:

docker compose exec backend python -m pip show matplotlib


============================================================
15. VERIFY IMPORTANT RUNTIME IMPORTS
============================================================

We used:

docker compose exec backend python -c "import mlflow.sklearn; import sklearn; import pandas; import numpy; print('Runtime ML imports: OK')"

WHAT THIS TESTS:

    mlflow.sklearn
    sklearn
    pandas
    numpy

If successful:

Runtime ML imports: OK

This is better than assuming that pip installation succeeded.

IMPORTANT PRINCIPLE:

Installation success != application success.

Always test the actual imports your application needs.


============================================================
16. CHECK DOCKER IMAGE LAYERS
============================================================

COMMAND:

docker history murphai-backend:latest

WHAT IT DOES:

Shows the layers that make up the Docker image.

This is extremely useful for optimization.

Our result showed roughly:

    Python base image       → ~109 MB
    system layer            → ~44.6 MB
    pip dependencies        → ~682 MB
    ML source               → ~7.53 MB
    backend source          → ~1.21 MB

The biggest layer was:

    pip install
        ↓
    ~682 MB

Therefore we knew that dependencies were the major source
of image size.

IMPORTANT:

Never optimize blindly.

First:

    docker history IMAGE

Then identify the largest layer.


============================================================
17. BUILD WITHOUT CACHE
============================================================

COMMAND:

docker compose build --no-cache backend

WHAT IT DOES:

Forces Docker to rebuild the backend image without using
previous Docker build cache.

Why useful?

Suppose you changed:

Dockerfile

and want a clean measurement.

Use:

docker compose build --no-cache backend


IMPORTANT:

This can take a long time because all dependencies may
need to be downloaded and installed again.

Do NOT assume the build is frozen just because:

    pip install

takes several minutes.

Watch the output.


============================================================
18. DOCKERFILE PYTHON OPTIMIZATION
============================================================

We changed:

FROM python:3.12-slim

and used:

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

MEANING:

PYTHONDONTWRITEBYTECODE=1

Prevents Python from creating .pyc bytecode files.

PYTHONUNBUFFERED=1

Makes Python output/logs appear immediately.

This is useful for containerized applications.


============================================================
19. --NO-COMPILE OPTIMIZATION
============================================================

We changed pip installation to:

RUN pip install --no-cache-dir --no-compile --upgrade pip \
    && pip install --no-cache-dir --no-compile -r requirements.txt

MEANING:

--no-cache-dir

Prevents pip from keeping its package download cache.

This helps reduce image size.

--no-compile

Prevents pip from compiling Python bytecode during installation.

This reduced our MurphAI image size significantly.

BEFORE:

297,934,707 bytes
≈ 297.9 MB

AFTER:

233,620,268 bytes
≈ 233.6 MB

Reduction:

≈ 64.3 MB

Approximately:

21.6% smaller


IMPORTANT REAL-WORLD LESSON:

Do not say:

"--no-compile always reduces Docker images by 21%."

That would be wrong.

The result depends on:

    - dependencies
    - Python packages
    - image structure
    - Python version
    - package contents

Always measure YOUR image.


============================================================
20. CHECK IMAGE SIZE AFTER OPTIMIZATION
============================================================

COMMAND:

docker image inspect murphai-backend:latest --format '{{.Size}}'

Workflow:

BEFORE:

docker image inspect murphai-backend:latest --format '{{.Size}}'

Make optimization.

Rebuild:

docker compose build --no-cache backend

AFTER:

docker image inspect murphai-backend:latest --format '{{.Size}}'


This is the correct optimization loop:

    Measure
       ↓
    Change
       ↓
    Build
       ↓
    Measure again
       ↓
    Verify application


============================================================
21. HEALTHCHECK
============================================================

Our Dockerfile contains:

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/', timeout=5)"

WHAT IT DOES:

Docker periodically checks:

    Is the MurphAI API responding?

If yes:

    healthy

If repeated checks fail:

    unhealthy


WHY IT MATTERS:

A container being:

    "running"

does NOT necessarily mean:

    "application is healthy"

The process can be alive while the application is broken.

Therefore:

    running != healthy


============================================================
22. CHECK HEALTH STATUS
============================================================

COMMAND:

docker compose ps

Look for:

    Up ... (healthy)

For more detailed health information:

docker inspect murphai-backend


You can search the output for:

    Health


============================================================
23. TEST THE APPLICATION FROM INSIDE CONTAINER
============================================================

Example:

docker compose exec backend python -c "import urllib.request; print(urllib.request.urlopen('http://127.0.0.1:8000/').read().decode())"

This tests the API from inside the container.

Useful when you want to distinguish:

    application problem

from:

    host/network/port problem


============================================================
24. TEST THE HOST → CONTAINER PORT
============================================================

If port mapping is:

    8000:8000

then host machine can access:

http://localhost:8000

Useful commands:

curl http://localhost:8000/

or:

curl http://localhost:8000/docs


Meaning:

HOST PORT : CONTAINER PORT

    8000 : 8000


============================================================
25. AUTHENTICATION TESTING
============================================================

Our `/ml/predict` endpoint requires authentication.

We intentionally tested it without authentication.

The result was:

HTTP 401 Unauthorized

This is EXPECTED.

Important lesson:

    401 does not automatically mean the application is broken.

It can mean:

    security is working correctly.


============================================================
26. RUN APPLICATION TESTS INSIDE DOCKER
============================================================

COMMAND:

docker compose exec backend pytest backend/tests/test_ml_api.py -v

This verifies the actual ML API.

Our result:

test_ml_prediction_success
    PASSED

test_ml_prediction_requires_authentication
    PASSED

test_ml_prediction_rejects_invalid_input
    PASSED

Final:

3 passed


This is much stronger than simply checking:

    container is running


We verified:

    API functionality
    authentication
    validation
    ML inference


============================================================
27. WHY TEST INSIDE THE CONTAINER?
============================================================

Your laptop environment and Docker environment are different.

Your laptop might have:

    Python X
    package Y
    environment Z

while Docker has:

    Python 3.12
    installed requirements
    Linux environment

Therefore:

    "It works on my Mac"

does NOT prove:

    "It works inside Docker"


The proper test is:

docker compose exec backend pytest ...


============================================================
28. DOCKER COMPOSE VOLUMES
============================================================

Example from MurphAI:

./murphai.db:/app/murphai.db

Meaning:

HOST:

./murphai.db

CONTAINER:

/app/murphai.db


This allows the database data to survive container recreation.


Another MurphAI volume:

./mlflow.db:/app/mlflow.db

This persists MLflow metadata.


============================================================
29. MLflow ARTIFACT VOLUME
============================================================

MurphAI currently uses:

./mlruns:/Users/manishkumar/Documents/Explorer/MurphAI/mlruns

This was required because the current local MLflow 3 setup
stored artifacts using that path.

IMPORTANT:

This is a LOCAL DEVELOPMENT SOLUTION.

It is NOT the final production architecture.

For production we should eventually use something like:

    MLflow Tracking Server
          ↓
    PostgreSQL metadata
          ↓
    S3/object storage for artifacts

Instead of a machine-specific local filesystem mount.


============================================================
30. DOCKER .dockerignore
============================================================

Our .dockerignore excludes things such as:

.venv/
.env
*.db
__pycache__/
.pytest_cache/
.git/
node_modules/
.DS_Store
mlruns/

WHY?

The Docker build context should contain only what the image
actually needs.

Benefits:

    - smaller build context
    - faster builds
    - smaller risk of leaking secrets
    - cleaner images
    - better caching


IMPORTANT:

`.dockerignore` is different from `.gitignore`.

.gitignore

    → controls what Git tracks

.dockerignore

    → controls what Docker receives as build context


============================================================
31. DOCKER BUILD CONTEXT
============================================================

Our Compose configuration:

build:
  context: .
  dockerfile: infrastructure/docker/Dockerfile

Meaning:

Docker build context:

    project root

Dockerfile:

    infrastructure/docker/Dockerfile


Therefore the Dockerfile can do:

COPY backend ./backend
COPY ml ./ml
COPY alembic ./alembic

because these directories exist inside the build context.


============================================================
32. DOCKERFILE COPY ORDER
============================================================

We use:

COPY requirements.txt .

RUN pip install ...

THEN:

COPY backend ./backend
COPY ml ./ml
...

WHY?

Docker caching.

If application source changes but requirements.txt doesn't:

Docker can reuse the dependency installation layer.

Therefore:

    COPY requirements.txt
          ↓
    pip install
          ↓
    COPY source code

is generally better than:

    COPY entire project
          ↓
    pip install


============================================================
33. CREATE NON-ROOT USER
============================================================

Dockerfile:

RUN useradd --create-home --shell /bin/bash murphai

Then:

RUN chown -R murphai:murphai /app

Then:

USER murphai

WHY chown?

Because files under /app initially belong to root.

The application user needs permission to access them.

Therefore:

    create user
       ↓
    give ownership
       ↓
    switch user


============================================================
34. CHECK IMAGE DETAILS
============================================================

COMMAND:

docker inspect murphai-backend:latest

This provides detailed metadata.

Useful information includes:

    - environment
    - entrypoint
    - command
    - exposed ports
    - architecture
    - layers
    - configuration
    - healthcheck


============================================================
35. CHECK RUNNING CONTAINER DETAILS
============================================================

COMMAND:

docker inspect murphai-backend

Useful when debugging:

    - mounts
    - environment
    - network
    - health
    - command
    - container configuration


============================================================
36. RESTART A SERVICE
============================================================

COMMAND:

docker compose restart backend

Useful when:

    - application process needs restarting
    - image did not change
    - configuration does not require rebuild


IMPORTANT:

If Dockerfile changes:

    restart

is NOT enough.

Use:

docker compose up --build -d


============================================================
37. REBUILD ONLY ONE SERVICE
============================================================

COMMAND:

docker compose build backend

Useful in multi-service projects.

Example:

    backend
    frontend
    redis
    worker

If only backend changed:

docker compose build backend


============================================================
38. FORCE COMPLETE REBUILD
============================================================

COMMAND:

docker compose build --no-cache backend

Use when:

    - testing Dockerfile changes
    - cache may be hiding problems
    - dependency installation changed
    - measuring image optimization
    - debugging strange build behavior


Don't use --no-cache every time.

It makes builds slower.


============================================================
39. CLEAN UP STOPPED CONTAINERS
============================================================

Useful commands:

docker container prune

Removes stopped containers.

Be careful.

It is destructive for stopped containers you may still want.


============================================================
40. REMOVE UNUSED IMAGES
============================================================

COMMAND:

docker image prune

Removes dangling/unused images depending on Docker's cleanup rules.

Be careful before using aggressive cleanup commands.

For example:

docker system prune

can remove more Docker resources.

Never blindly run destructive Docker cleanup commands
on an important environment.


============================================================
41. COMPLETE REAL-WORLD DEBUGGING FLOW
============================================================

Suppose your Docker application is broken.

Do NOT immediately rebuild everything.

Use this sequence:

STEP 1:

docker compose ps

Check:

    Is container running?
    Is it healthy?


STEP 2:

docker compose logs backend

Check:

    application errors?
    import errors?
    database errors?


STEP 3:

docker compose exec backend whoami

Check:

    correct runtime user?


STEP 4:

docker compose exec backend python --version

Check:

    correct Python?


STEP 5:

docker compose exec backend python -m pip list

Check:

    required packages?


STEP 6:

docker compose exec backend python -c "import ..."

Check:

    required imports?


STEP 7:

Run application tests:

docker compose exec backend pytest -v


STEP 8:

Only if necessary:

docker compose build --no-cache backend


STEP 9:

Restart:

docker compose up -d


This prevents random debugging.


============================================================
42. REAL-WORLD DOCKER DEVELOPMENT LOOP
============================================================

When developing a project:

    Change code
       ↓
    docker compose up -d
       ↓
    docker compose ps
       ↓
    docker compose logs
       ↓
    Test API
       ↓
    Run tests
       ↓
    Fix
       ↓
    Repeat


============================================================
43. REAL-WORLD DOCKER PRODUCTION CHECKLIST
============================================================

Before calling a Docker setup production-ready:

[ ] Small appropriate base image

[ ] .dockerignore exists

[ ] Secrets are NOT inside image

[ ] .env is NOT committed

[ ] Application does NOT run as root

[ ] Healthcheck exists

[ ] Logs are visible

[ ] Dependencies are pinned appropriately

[ ] Image size measured

[ ] Application tests pass inside container

[ ] Security tested

[ ] No unnecessary packages

[ ] Volumes designed correctly

[ ] Database persistence designed correctly

[ ] Production secrets management planned

[ ] Resource limits considered

[ ] Image tagged with version

[ ] Image pushed to registry

[ ] CI/CD builds image

[ ] Deployment strategy defined


============================================================
44. MOST IMPORTANT COMMANDS TO MEMORIZE
============================================================

You do NOT need to memorize 50 commands.

Master these:

1.

docker images

→ See local images.


2.

docker ps

→ See running containers.


3.

docker ps -a

→ See all containers.


4.

docker compose up -d

→ Start application.


5.

docker compose up --build -d

→ Build + start.


6.

docker compose down

→ Stop/remove Compose containers.


7.

docker compose ps

→ Check Compose services.


8.

docker compose logs backend

→ Debug logs.


9.

docker compose exec backend bash

→ Enter container.


10.

docker compose exec backend <command>

→ Execute command inside container.


11.

docker image inspect IMAGE

→ Inspect image.


12.

docker history IMAGE

→ Inspect image layers.


13.

docker compose build --no-cache backend

→ Clean rebuild.


14.

docker compose exec backend pytest -v

→ Test application inside container.


============================================================
45. THE CORE MENTAL MODEL
============================================================

Remember Docker like this:

DOCKERFILE
    ↓
    defines how image is built

IMAGE
    ↓
    packaged application environment

CONTAINER
    ↓
    running instance of image

COMPOSE
    ↓
    manages one or more containers/services

VOLUME
    ↓
    persistent data

NETWORK
    ↓
    communication between services

HEALTHCHECK
    ↓
    tells Docker whether application is healthy


============================================================
46. MURPHAI EXAMPLE
============================================================

Our architecture currently looks like:

                    Docker Compose
                         │
                         ↓
                ┌──────────────────┐
                │ murphai-backend  │
                │                  │
                │ FastAPI          │
                │ ML inference     │
                │ MLflow           │
                │ SQLAlchemy       │
                └────────┬─────────┘
                         │
              ┌──────────┼──────────┐
              ↓          ↓          ↓
          murphai.db  mlflow.db   mlruns
           volume      volume      volume


The container:

    runs as murphai user

    listens on:

        8000

    has:

        HEALTHCHECK

    contains:

        Python
        FastAPI
        ML stack
        MLflow


============================================================
47. OUR FINAL MURPHAI DOCKER CHECKPOINT
============================================================

We completed:

    Docker image
        ↓
    Docker Compose
        ↓
    Healthcheck
        ↓
    Non-root user
        ↓
    .dockerignore
        ↓
    Image optimization
        ↓
    Runtime verification
        ↓
    ML import verification
        ↓
    Authentication verification
        ↓
    ML API testing
        ↓
    Git commit
        ↓
    GitHub push


Final image measurement:

    233,620,268 bytes

Approximately:

    233.6 MB


Git commit:

    8de3a71

Message:

    add Docker containerization


============================================================
48. GOLDEN RULES
============================================================

RULE 1:

Don't optimize blindly.

Measure first.


RULE 2:

Don't trust "container is running".

Check health.


RULE 3:

Don't trust "pip install succeeded".

Test imports.


RULE 4:

Don't trust "works on my machine".

Test inside Docker.


RULE 5:

Don't run production applications as root
unless there is a specific reason.


RULE 6:

Don't put secrets inside Dockerfile.


RULE 7:

Don't commit .env.


RULE 8:

Use .dockerignore.


RULE 9:

Use Docker logs before randomly rebuilding.


RULE 10:

When optimizing:

    BEFORE
       ↓
    CHANGE
       ↓
    BUILD
       ↓
    MEASURE
       ↓
    TEST


RULE 11:

A smaller image is NOT automatically a better image.

Correctness + security + reproducibility + maintainability
come first.


RULE 12:

Local Docker architecture and production architecture
are not necessarily the same.

MurphAI's current MLflow filesystem setup is acceptable
for local development, but production should eventually
use proper infrastructure.


============================================================
49. ONE-LINE RECALL
============================================================

When you forget Docker, remember:

    BUILD → RUN → CHECK → LOG → EXEC → TEST → OPTIMIZE → VERIFY


That is the real-world Docker workflow.

'''