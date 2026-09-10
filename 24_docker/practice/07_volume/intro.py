"""
===========================================================
DOCKER VOLUMES — THEORY + COMMANDS
===========================================================

1. WHAT IS A DOCKER VOLUME?
-----------------------------------------------------------
A Docker volume is a permanent storage area managed by
Docker.

Normally:

    Container
        |
        └── Data

If the container is deleted, the data inside the container
can also be lost.

A volume separates DATA from the CONTAINER.

    Container
        |
        └── Volume
              |
              └── Data

The container can be deleted and recreated, but the volume
and its data can remain.

-----------------------------------------------------------

2. WHY DO WE NEED VOLUMES?
-----------------------------------------------------------

Containers are designed to be temporary/recreatable.

For example:

    Container A
        ↓
    database data

If Container A is deleted:

    Container A ❌
    database data ❌

But with a volume:

    Container A
        ↓
    Docker Volume
        ↓
    database data

Delete Container A:

    Container A ❌
    Docker Volume ✅
    database data ✅

Create a new container and attach the same volume:

    Container B
        ↓
    Docker Volume
        ↓
    old database data ✅


-----------------------------------------------------------

3. REAL-WORLD EXAMPLE
-----------------------------------------------------------

Imagine a PostgreSQL database running inside Docker.

Without a volume:

    PostgreSQL Container
          ↓
       Database
          ↓
    Container deleted
          ↓
    Database data lost ❌


With a volume:

    PostgreSQL Container
          ↓
    PostgreSQL Volume
          ↓
       Database

    Container deleted
          ↓
    Volume remains
          ↓
    Database data remains ✅


This is extremely important for databases.


-----------------------------------------------------------

4. IMPORTANT IDEA
-----------------------------------------------------------

Container = Application

Volume = Persistent Data

Example:

    PostgreSQL Container
            +
    PostgreSQL Volume

The container runs PostgreSQL.

The volume stores PostgreSQL's data.


-----------------------------------------------------------

5. CREATE A VOLUME
-----------------------------------------------------------

Command:

    docker volume create mydata

Example:

    docker volume create mydata

Check volumes:

    docker volume ls

You should see:

    DRIVER    VOLUME NAME
    local     mydata


-----------------------------------------------------------

6. INSPECT A VOLUME
-----------------------------------------------------------

Command:

    docker volume inspect mydata

This shows information about the volume such as:

    - Name
    - Driver
    - Mountpoint
    - Creation information


-----------------------------------------------------------

7. ATTACH A VOLUME TO A CONTAINER
-----------------------------------------------------------

Syntax:

    docker run -it \
        --name container-name \
        -v volume-name:/container/path \
        image-name \
        command

Example:

    docker run -it \
        --name volume-test \
        -v mydata:/data \
        alpine \
        sh

Meaning:

    mydata       → Docker volume
    /data        → directory inside container
    alpine       → Docker image
    sh           → shell

So:

    mydata
       ↓
    /data inside container


-----------------------------------------------------------

8. WRITE DATA INTO THE VOLUME
-----------------------------------------------------------

Inside the container:

    echo "Hello from Docker Volume" > /data/test.txt

Read it:

    cat /data/test.txt

Output:

    Hello from Docker Volume


-----------------------------------------------------------

9. DELETE THE CONTAINER
-----------------------------------------------------------

Exit container:

    exit

Then:

    docker rm volume-test

The container is gone.

But:

    mydata

still exists.


-----------------------------------------------------------

10. PROVE THAT THE DATA PERSISTED
-----------------------------------------------------------

Create another container using the SAME volume:

    docker run -it \
        --name volume-test-2 \
        -v mydata:/data \
        alpine \
        sh

Now:

    cat /data/test.txt

Output:

    Hello from Docker Volume

This proves:

    Container ❌
         ↓
    Volume ✅
         ↓
    Data ✅


-----------------------------------------------------------

11. CONTAINER STORAGE vs VOLUME STORAGE
-----------------------------------------------------------

Container storage:

    Container
       ↓
      Data

Container deleted:

    Data ❌


Volume storage:

    Container
       ↓
     Volume
       ↓
      Data

Container deleted:

    Volume ✅
    Data ✅


-----------------------------------------------------------

12. WHEN SHOULD WE USE VOLUMES?
-----------------------------------------------------------

Use Docker volumes when data must survive container
recreation.

Common examples:

    PostgreSQL
    MySQL
    MongoDB
    Redis
    Application uploads
    User-generated files
    Persistent application data


Example:

    PostgreSQL
         ↓
    postgres_data volume

    MongoDB
         ↓
    mongo_data volume


-----------------------------------------------------------

13. WHEN DO WE NOT NEED A VOLUME?
-----------------------------------------------------------

You usually don't need a volume for temporary data.

Examples:

    Temporary files
    Cache
    Build artifacts
    Short-lived test data


If the data can safely disappear when the container
disappears, a volume may not be necessary.


-----------------------------------------------------------

14. REMOVE A VOLUME
-----------------------------------------------------------

Command:

    docker volume rm mydata

IMPORTANT:

Removing a volume permanently removes the data stored
inside that volume.

So be careful.

Check first:

    docker volume ls

Then remove:

    docker volume rm mydata


-----------------------------------------------------------

15. REMOVE UNUSED VOLUMES
-----------------------------------------------------------

Command:

    docker volume prune

This removes unused Docker volumes.

Be careful because unused volumes may contain data
you still want.


-----------------------------------------------------------

16. COMPLETE PRACTICE FLOW
-----------------------------------------------------------

Step 1:

    docker volume create mydata

Step 2:

    docker volume ls

Step 3:

    docker run -it \
        --name volume-test \
        -v mydata:/data \
        alpine \
        sh

Step 4:

Inside container:

    echo "Hello from Docker Volume" > /data/test.txt

Step 5:

    cat /data/test.txt

Step 6:

    exit

Step 7:

    docker rm volume-test

Step 8:

Create another container:

    docker run -it \
        --name volume-test-2 \
        -v mydata:/data \
        alpine \
        sh

Step 9:

    cat /data/test.txt

If you see:

    Hello from Docker Volume

your volume is working correctly.


===========================================================
MOST IMPORTANT COMMANDS TO REMEMBER
===========================================================

Create:

    docker volume create mydata

List:

    docker volume ls

Inspect:

    docker volume inspect mydata

Attach:

    docker run -it \
        -v mydata:/data \
        alpine sh

Remove:

    docker volume rm mydata

Remove unused:

    docker volume prune


===========================================================
ONE-LINE MEMORY TRICK
===========================================================

Container = Temporary Environment

Volume = Persistent Storage

Container can die.

Volume keeps the data alive.


===========================================================
MURPHAI CONNECTION
===========================================================

Later in MurphAI:

    FastAPI Container
          ↓
    PostgreSQL Container
          ↓
    PostgreSQL Volume
          ↓
    Users / Workers / Jobs /
    Evidence / Payments / Reputation

If PostgreSQL's container is recreated:

    PostgreSQL Container ❌
            ↓
    PostgreSQL Volume ✅
            ↓
    MurphAI database data ✅

This is why volumes are important in real-world Docker
applications.
===========================================================
"""