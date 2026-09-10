"""
========================================================
02 - IMAGES AND CONTAINERS
========================================================
"""


"""
========================================================
IMAGE
========================================================

An IMAGE is a blueprint/template.

Example:

ubuntu image
python image
nginx image

An image contains everything required
to create a container.
"""


"""
========================================================
CONTAINER
========================================================

A CONTAINER is a running/created instance
of an image.

Think:

IMAGE
  ↓
Blueprint

CONTAINER
  ↓
Actual running instance
"""


"""
========================================================
REAL WORLD ANALOGY
========================================================

IMAGE = Class

CONTAINER = Object

Example:

Python class:

class Car:
    pass

Objects:

car1 = Car()
car2 = Car()

Similarly:

Ubuntu IMAGE
     ↓
     ├── Container 1
     ├── Container 2
     └── Container 3
"""


"""
========================================================
CREATE AND RUN A CONTAINER
========================================================

docker run ubuntu

This:

1. Finds ubuntu image.
2. Creates a container.
3. Starts it.
4. Runs its default command.

The container may exit immediately because
its main process finishes.
"""


"""
========================================================
INTERACTIVE CONTAINER
========================================================

docker run -it ubuntu bash

Meaning:

-i
Interactive

-t
Allocate terminal

ubuntu
Image

bash
Run Bash shell
"""


"""
========================================================
NAMING A CONTAINER
========================================================

docker run -it --name my-ubuntu ubuntu bash

Now the container has a custom name:

my-ubuntu
"""


"""
========================================================
SEE CONTAINERS
========================================================

docker ps

Only running containers.

docker ps -a

All containers.
"""


"""
========================================================
SEE IMAGES
========================================================

docker images

Shows locally available images.
"""


"""
========================================================
IMPORTANT RELATIONSHIP
========================================================

IMAGE
  ↓
docker run
  ↓
CONTAINER
  ↓
application runs
  ↓
container may stop
"""


"""
========================================================
ONE IMAGE → MANY CONTAINERS
========================================================

ubuntu IMAGE
     │
     ├──── Container A
     │
     ├──── Container B
     │
     └──── Container C

All containers can be created
from the same image.
"""