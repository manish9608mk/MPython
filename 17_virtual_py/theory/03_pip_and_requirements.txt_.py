'''
Suppose: 1. You already installed google-genai ✅
Now create requirements.txt from your current virtual environment:
python -m pip freeze > requirements.txt
This creates:
ex-
01_project/
├── .venv/
├── code_files/
└── requirements.txt

2. Check the file:
cat requirements.txt
You'll see packages like: google-genai==2.20.0 or......
It may contain all packages installed in your .venv, including dependencies of google-genai. That's normal.


3. When another person clones your project
They create and activate their own .venv, then run:
python -m pip install -r requirements.txt
That installs the dependencies required by your project.


⭐ Important distinction:
To create/update the file:
python -m pip freeze > requirements.txt

To install from the file:
python -m pip install -r requirements.txt
'''





'''
Essential Python Virtual Environment Workflow - 

Remember this workflow:

python3 -m venv .venv
        ↓
source .venv/bin/activate
        ↓
pip install django
        ↓
pip freeze > requirements.txt


When you move the project to a new machine/server:

python3 -m venv .venv
        ↓
source .venv/bin/activate
        ↓
pip install -r requirements.txt


One-line memory trick:

.venv = Isolated environment

pip = Package manager

requirements.txt = Dependency list

pip freeze = Installed packages → requirements.txt

pip install -r = requirements.txt → Installed packages


OR,
'''





'''
MUST REMEMBER — Python Virtual Environment

1. Create a virtual environment:

python3 -m venv .venv


2. Activate it on macOS/Linux:

source .venv/bin/activate


3. Install a package:

pip install package_name


4. Save installed dependencies:

pip freeze > requirements.txt


5. Install all dependencies from requirements.txt:

pip install -r requirements.txt


6. Deactivate:

deactivate


Memory:

.venv = Isolated environment

pip = Package manager

requirements.txt = Project dependency list

pip freeze > requirements.txt
    = Save installed packages

pip install -r requirements.txt
    = Install all packages from the file
'''





'''
IN DETAILED -  PYTHON VIRTUAL ENVIRONMENT, PIP & REQUIREMENTS.TXT

1. WHAT IS A VIRTUAL ENVIRONMENT?
------------------------------------------------------------

A virtual environment is an isolated Python environment
created specifically for a project.

It allows each project to have its own:

    - Python packages
    - Package versions
    - Dependencies

Without affecting other Python projects on the system.


Example:

Project A requires:

    Django==5.2

Project B requires:

    Django==6.1

If both projects use the same global Python environment,
there can be version conflicts.

Virtual environments solve this problem.


------------------------------------------------------------
2. WHY DO WE NEED A VIRTUAL ENVIRONMENT?
------------------------------------------------------------

Suppose we have:

Project A:

    Django==5.2

Project B:

    Django==6.1


If we install Django globally:

    pip install django

there is only one global Django installation.

But different projects may require different versions.

Therefore:

    Project A -> .venv -> Django 5.2
    Project B -> .venv -> Django 6.1


Each project gets its own isolated dependencies.


------------------------------------------------------------
3. CREATE A VIRTUAL ENVIRONMENT
------------------------------------------------------------

Command:

    python3 -m venv .venv


Explanation:

    python3
        -> Runs Python 3

    -m
        -> Runs a Python module

    venv
        -> Python's built-in virtual environment module

    .venv
        -> Name of the virtual environment directory


You can use another name:

    python3 -m venv myenv

But `.venv` is a common convention.


------------------------------------------------------------
4. PROJECT STRUCTURE
------------------------------------------------------------

A typical project can look like:

project/
│
├── .venv/
│
├── src/
│   └── main.py
│
├── requirements.txt
│
└── README.md


`.venv`
    -> Contains the project's isolated Python environment.

`src`
    -> Contains source code.

`requirements.txt`
    -> Contains project dependencies.

`README.md`
    -> Contains project documentation.


------------------------------------------------------------
5. ACTIVATE VIRTUAL ENVIRONMENT
------------------------------------------------------------

On macOS/Linux:

    source .venv/bin/activate


After activation, terminal usually shows:

    (.venv)


Example:

    (.venv) user@Mac project %


This indicates that the virtual environment is active.


------------------------------------------------------------
6. DEACTIVATE VIRTUAL ENVIRONMENT
------------------------------------------------------------

Command:

    deactivate


After this:

    (.venv)

will disappear from the terminal prompt.


Important:

Deactivating does NOT delete the virtual environment.

It only stops using it for the current terminal session.


------------------------------------------------------------
7. WHAT HAPPENS AFTER ACTIVATION?
------------------------------------------------------------

When `.venv` is activated:

    pip install django

installs Django inside:

    project/.venv/


Instead of installing it into the global Python environment.


This gives us:

    Global Python
        |
        ├── Project A .venv
        │      └── Django 5.2
        |
        └── Project B .venv
               └── Django 6.1


------------------------------------------------------------
8. WHAT IS pip?
------------------------------------------------------------

`pip` is Python's package installer.

It is used to:

    - Install packages
    - Upgrade packages
    - Remove packages
    - List installed packages
    - Manage project dependencies


Example:

    pip install django


------------------------------------------------------------
9. INSTALL A PACKAGE
------------------------------------------------------------

Command:

    pip install django


This downloads Django and installs it into the currently
active Python environment.


If `.venv` is active:

    pip install django

will install Django inside `.venv`.


------------------------------------------------------------
10. INSTALL A SPECIFIC VERSION
------------------------------------------------------------

You can install a specific package version.

Example:

    pip install django==6.1


Meaning:

    Install exactly Django version 6.1.


Other examples:

    pip install pymongo==4.17.0

    pip install requests==2.32.4


------------------------------------------------------------
11. VERSION SPECIFIERS
------------------------------------------------------------

Common version operators:

    ==      Exactly this version
    >=      This version or newer
    <=      This version or older
    >       Newer than this version
    <       Older than this version


Examples:

    django==6.1

    django>=5.0

    django>=5.0,<7.0


`==` is commonly used in requirements.txt when exact
reproducibility is desired.


------------------------------------------------------------
12. INSTALL MULTIPLE PACKAGES
------------------------------------------------------------

You can install multiple packages in one command:

    pip install django pymongo requests


This installs all specified packages.


------------------------------------------------------------
13. CHECK INSTALLED PACKAGES
------------------------------------------------------------

Command:

    pip list


Example output:

    Package       Version
    ---------------------
    Django        6.1
    pymongo       4.17.0
    requests      2.32.4


This shows packages currently installed in the active
environment.


------------------------------------------------------------
14. WHAT IS requirements.txt?
------------------------------------------------------------

`requirements.txt` is a text file that contains the Python
dependencies required by a project.


Example:

    Django==6.1
    pymongo==4.17.0
    dnspython==2.8.0


It acts like a dependency list for the project.


Think of it as:

    requirements.txt
            =
    Project dependency list


------------------------------------------------------------
15. WHY DO WE NEED requirements.txt?
------------------------------------------------------------

Suppose you create a project and install:

    Django
    pymongo
    requests
    numpy


Your computer has all these packages.

But if you send the project to another computer,
the other computer may not have them installed.


Instead of telling the person:

    pip install django
    pip install pymongo
    pip install requests
    pip install numpy


you provide:

    requirements.txt


Then they can run:

    pip install -r requirements.txt


and install everything listed in the file.


------------------------------------------------------------
16. pip freeze
------------------------------------------------------------

Command:

    pip freeze


It displays installed packages in requirements-file format.


Example:

    asgiref==3.12.1
    Django==6.1
    dnspython==2.8.0
    pymongo==4.17.0
    sqlparse==0.6.0


------------------------------------------------------------
17. SAVE INSTALLED PACKAGES TO requirements.txt
------------------------------------------------------------

Command:

    pip freeze > requirements.txt


Meaning:

    pip freeze
        -> Gets installed packages

    >
        -> Redirects output into a file

    requirements.txt
        -> File where the output is saved


Example:

    pip freeze > requirements.txt


Now requirements.txt contains the installed packages.


------------------------------------------------------------
18. IMPORTANT DIFFERENCE
------------------------------------------------------------

These commands do DIFFERENT things.


Command:

    pip install django

MEANING:

    Install Django.


Command:

    pip freeze

MEANING:

    Show installed packages.


Command:

    pip freeze > requirements.txt

MEANING:

    Save installed packages into requirements.txt.


Command:

    pip install -r requirements.txt

MEANING:

    Install all packages listed in requirements.txt.


------------------------------------------------------------
19. WHAT DOES -r MEAN?
------------------------------------------------------------

In:

    pip install -r requirements.txt


`-r` means:

    requirements file


It tells pip:

    Read package requirements from this file
    and install them.


------------------------------------------------------------
20. INSTALL EVERYTHING FROM requirements.txt
------------------------------------------------------------

Suppose requirements.txt contains:

    Django==6.1
    pymongo==4.17.0
    requests==2.32.4


Run:

    pip install -r requirements.txt


pip will read the file and install:

    Django
    pymongo
    requests


automatically.


You do NOT need to install them one by one.


------------------------------------------------------------
21. COMPLETE PROJECT WORKFLOW
------------------------------------------------------------

Recommended workflow:

Step 1:

    Create project directory.


Step 2:

    Create virtual environment:

    python3 -m venv .venv


Step 3:

    Activate:

    source .venv/bin/activate


Step 4:

    Install required packages:

    pip install django


Step 5:

    Install another package:

    pip install pymongo


Step 6:

    Save dependencies:

    pip freeze > requirements.txt


Now the project contains:

    project/
    ├── .venv/
    ├── src/
    └── requirements.txt


------------------------------------------------------------
22. ANOTHER MACHINE
------------------------------------------------------------

Suppose you upload your project to GitHub.

Usually you DO NOT upload `.venv`.

Another machine clones the project:

    git clone <repository>


The project may contain:

    project/
    ├── src/
    ├── requirements.txt
    └── README.md


The other machine creates its own environment:

    python3 -m venv .venv


Activate it:

    source .venv/bin/activate


Then:

    pip install -r requirements.txt


Now all project dependencies are installed.


------------------------------------------------------------
23. WHY DON'T WE USUALLY COMMIT .venv TO GIT?
------------------------------------------------------------

`.venv` contains the actual installed Python environment.

It can contain many files and packages.

It is:

    - Large
    - Machine-specific
    - Unnecessary to share
    - Reproducible using requirements.txt


Therefore, we normally add:

    .venv/


to `.gitignore`.


Instead of sharing `.venv`, we share:

    requirements.txt


Then another developer creates a new `.venv`
and installs the dependencies.


------------------------------------------------------------
24. .gitignore
------------------------------------------------------------

A `.gitignore` file tells Git which files/directories
should not be tracked.


Example:

    .venv/
    __pycache__/
    *.pyc


This prevents the virtual environment and Python cache
files from being committed to Git.


------------------------------------------------------------
25. INSTALLING A NEW PACKAGE
------------------------------------------------------------

Suppose Django is already installed.

Now you want:

    requests


Run:

    pip install requests


Then update requirements.txt:

    pip freeze > requirements.txt


Now requests will be included.


------------------------------------------------------------
26. IMPORTANT: requirements.txt DOES NOT AUTOMATICALLY
    UPDATE
------------------------------------------------------------

Installing:

    pip install django


does NOT automatically modify:

    requirements.txt


You must explicitly update it:

    pip freeze > requirements.txt


This is why you previously installed Django but initially
did not see it in requirements.txt.


------------------------------------------------------------
27. COMPLETE EXAMPLE
------------------------------------------------------------

Initially:

requirements.txt

    dnspython==2.8.0
    pymongo==4.17.0


Install Django:

    pip install django


Now the environment contains:

    dnspython
    pymongo
    Django
    asgiref
    sqlparse


But requirements.txt may still contain only the old list.


To update it:

    pip freeze > requirements.txt


Now it can contain:

    asgiref==3.12.1
    Django==6.1
    dnspython==2.8.0
    pymongo==4.17.0
    sqlparse==0.6.0


------------------------------------------------------------
28. PACKAGE DEPENDENCIES
------------------------------------------------------------

A package can depend on other packages.


For example:

    Django
       |
       ├── asgiref
       └── sqlparse


When you run:

    pip install django


pip can automatically install Django's required
dependencies as well.


That's why after installing Django you saw:

    asgiref
    Django
    sqlparse


in `pip list`.


------------------------------------------------------------
29. pip list vs pip freeze
------------------------------------------------------------

`pip list`:

    pip list


is mainly useful for viewing installed packages in a
human-friendly table.


Example:

    Package     Version
    Django      6.1


`pip freeze`:

    pip freeze


produces output suitable for dependency files:

    Django==6.1


So:

    pip list
        -> Human-friendly package listing

    pip freeze
        -> Requirements-style package listing


------------------------------------------------------------
30. UPGRADE A PACKAGE
------------------------------------------------------------

To upgrade:

    pip install --upgrade django


or:

    pip install -U django


Both mean upgrade the package.


------------------------------------------------------------
31. UNINSTALL A PACKAGE
------------------------------------------------------------

Command:

    pip uninstall django


pip will ask for confirmation.

After uninstalling, update requirements.txt if necessary:

    pip freeze > requirements.txt


------------------------------------------------------------
32. CHECK pip VERSION
------------------------------------------------------------

Command:

    pip --version


Example:

    pip 26.x.x from .../.venv/...


This can also help verify which environment's pip
you are using.


------------------------------------------------------------
33. VERIFY WHICH PYTHON IS BEING USED
------------------------------------------------------------

macOS/Linux:

    which python


When `.venv` is active, it should point to something
inside:

    .venv/bin/python


Example:

    /project/.venv/bin/python


This confirms that your virtual environment is active.


------------------------------------------------------------
34. VERIFY WHICH pip IS BEING USED
------------------------------------------------------------

Command:

    which pip


When `.venv` is active, it should point inside:

    .venv/bin/pip


This is useful when debugging package installation issues.


------------------------------------------------------------
35. STORAGE
------------------------------------------------------------

Virtual environments do consume storage because packages
are installed inside them.

For example:

    Django
    NumPy
    Pandas
    PyTorch
    TensorFlow


can take different amounts of storage.


However, the storage belongs to the virtual environment.


If a virtual environment is no longer needed, it can simply
be deleted.


Example:

    rm -rf .venv


Then create a new one:

    python3 -m venv .venv

and reinstall dependencies:

    pip install -r requirements.txt


IMPORTANT:

Do NOT run `rm -rf .venv` unless you are sure you want to
delete that virtual environment.


------------------------------------------------------------
36. GLOBAL PACKAGE VS VIRTUAL ENVIRONMENT PACKAGE
------------------------------------------------------------

Global installation:

    pip install django


when no virtual environment is active may install Django
into the global Python environment.

Virtual environment installation:

    (.venv)
    pip install django


installs Django into that project's virtual environment.


Best practice:

    Use a virtual environment for each project.


------------------------------------------------------------
37. BASIC COMMAND CHEAT SHEET
------------------------------------------------------------

Create environment:

    python3 -m venv .venv


Activate:

    source .venv/bin/activate


Deactivate:

    deactivate


Install package:

    pip install django


Install specific version:

    pip install django==6.1


Install multiple packages:

    pip install django requests pymongo


List packages:

    pip list


Freeze packages:

    pip freeze


Save dependencies:

    pip freeze > requirements.txt


Install dependencies:

    pip install -r requirements.txt


Upgrade package:

    pip install --upgrade django


Uninstall package:

    pip uninstall django


Check Python:

    which python


Check pip:

    which pip


Check pip version:

    pip --version


------------------------------------------------------------
38. MOST IMPORTANT CONCEPT
------------------------------------------------------------

Remember this relationship:

    Virtual Environment
            |
            ↓
       .venv/
            |
            ↓
    Isolated packages
            |
            ↓
       pip manages them
            |
            ↓
    pip freeze
            |
            ↓
    requirements.txt
            |
            ↓
    pip install -r requirements.txt
            |
            ↓
    Recreate dependencies
    on another machine


------------------------------------------------------------
39. REAL-WORLD DEVELOPMENT FLOW
------------------------------------------------------------

Developer creates project:

    python3 -m venv .venv

Activate:

    source .venv/bin/activate

Install dependencies:

    pip install django
    pip install pymongo
    pip install requests

Save dependencies:

    pip freeze > requirements.txt

Add `.venv/` to `.gitignore`.

Push project to GitHub.

Another developer:

    git clone <project>

Create environment:

    python3 -m venv .venv

Activate:

    source .venv/bin/activate

Install everything:

    pip install -r requirements.txt


Now both developers have the required project
dependencies.


------------------------------------------------------------
40. KEY INTERVIEW POINTS
------------------------------------------------------------

Q: What is a virtual environment?

A:

A virtual environment is an isolated Python environment
that allows a project to maintain its own dependencies and
package versions.


Q: Why use virtual environments?

A:

To prevent dependency and version conflicts between
different Python projects.


Q: What is pip?

A:

pip is Python's package installer used to install and
manage Python packages.


Q: What is requirements.txt?

A:

A file containing the dependencies required by a Python
project, usually with their versions.


Q: What does pip freeze do?

A:

It outputs installed packages and their versions in a
requirements-file-compatible format.


Q: What does this do?

    pip freeze > requirements.txt

A:

It saves the currently installed packages and versions
into `requirements.txt`.


Q: What does this do?

    pip install -r requirements.txt

A:

It reads the requirements file and installs all listed
dependencies.


Q: Why don't we commit .venv to Git?

A:

Because the environment is machine-specific and can be
recreated from dependency files such as requirements.txt.


------------------------------------------------------------
41. GOLDEN RULE
------------------------------------------------------------

For every Python project:

    Create .venv
        ↓
    Activate .venv
        ↓
    Install packages
        ↓
    Freeze dependencies
        ↓
    Save requirements.txt
        ↓
    Don't commit .venv
        ↓
    Commit requirements.txt


============================================================
END
============================================================
'''