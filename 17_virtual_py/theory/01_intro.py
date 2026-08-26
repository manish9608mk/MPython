'''
important commands:

- Go to your project
cd 17_virtual_py

- Create venv — only once
python3 -m venv venv

- Activate — whenever you open a new terminal
source venv/bin/activate

- Verify
which python3

- Install packages
python3 -m pip install <package>

- Leave environment
deactivate
'''


# ============================================================
#                 PYTHON VIRTUAL ENVIRONMENT
# ============================================================


# ============================================================
# 1. WHAT IS A VIRTUAL ENVIRONMENT?
# ============================================================

# A Virtual Environment is an isolated Python environment
# created for a particular project.
#
# It allows each project to have its own:
# - Python packages
# - Package versions
# - Dependencies
#
# Example:
#
# Project A needs:
#     requests==2.31.0
#
# Project B needs:
#     requests==2.32.0
#
# Without virtual environments, different projects can
# interfere with each other.
#
# With virtual environments:
#
#     Project A
#         └── venv
#             └── requests 2.31.0
#
#     Project B
#         └── venv
#             └── requests 2.32.0
#
# They are isolated from each other.


# ============================================================
# 2. WHY DO WE NEED VIRTUAL ENVIRONMENTS?
# ============================================================

# Python projects usually depend on external packages.
#
# Examples:
#
#     numpy
#     pandas
#     requests
#     flask
#     fastapi
#     django
#     torch
#     tensorflow
#
# Different projects may require different versions
# of the same package.
#
# Example:
#
# Project A:
#     Django 4.x
#
# Project B:
#     Django 5.x
#
# Installing everything globally can create dependency
# conflicts.
#
# A virtual environment solves this problem by keeping
# project dependencies isolated.


# ============================================================
# 3. GLOBAL PYTHON vs VIRTUAL ENVIRONMENT
# ============================================================

# GLOBAL PYTHON
#
# Your Mac has a Python installation.
#
# Example:
#
#     /Library/Frameworks/Python.framework/...
#
# Packages installed globally may be available to
# many projects.
#
#
# VIRTUAL ENVIRONMENT
#
# A project can have its own Python environment.
#
# Example:
#
#     my_project/
#     ├── venv/
#     ├── app.py
#     └── requirements.txt
#
# Packages installed while venv is active are installed
# inside that environment.


# ============================================================
# 4. WHAT IS venv?
# ============================================================

# Python already provides a built-in module called:
#
#     venv
#
# Therefore, for normal Python virtual environments,
# you DO NOT need to install the "virtualenv" package.
#
# Modern Python provides:
#
#     python3 -m venv
#
# This is the standard approach for creating a basic
# virtual environment.


# ============================================================
# 5. CREATE A VIRTUAL ENVIRONMENT ON macOS
# ============================================================

# First, go to your project directory.
#
# Example:
#
#     cd 17_virtual_py
#
# Then create the virtual environment:
#
#     python3 -m venv venv
#
#
# IMPORTANT:
#
# "venv" appears twice for two different reasons:
#
#     python3 -m venv venv
#                  ↑    ↑
#                  |    |
#                  |    └── Name of the environment folder
#                  |
#                  └── Python's built-in venv module
#
#
# You can actually choose another name:
#
#     python3 -m venv myenv
#
# Then the folder will be:
#
#     myenv/
#
#
# Common convention:
#
#     python3 -m venv venv
#
# because "venv" is short and universally recognizable.


# ============================================================
# 6. WHAT GETS CREATED?
# ============================================================

# After:
#
#     python3 -m venv venv
#
# You will get something similar to:
#
#     project/
#     │
#     ├── venv/
#     │   ├── bin/
#     │   ├── include/
#     │   ├── lib/
#     │   └── pyvenv.cfg
#     │
#     └── app.py
#
#
# The venv directory contains the isolated environment.


# ============================================================
# 7. ACTIVATE THE VIRTUAL ENVIRONMENT ON macOS
# ============================================================

# On macOS/Linux:
#
#     source venv/bin/activate
#
#
# After activation, your terminal usually looks like:
#
#     (venv) username@MacBook project %
#
#
# The "(venv)" means that the virtual environment is active.


# ============================================================
# 8. IF THE venv IS INSIDE ANOTHER FOLDER
# ============================================================

# Suppose your structure is:
#
#     MPython/
#     └── 17_virtual_py/
#         ├── theory/
#         └── venv/
#
# If your terminal is currently inside:
#
#     MPython/
#
# activate using:
#
#     source 17_virtual_py/venv/bin/activate
#
#
# If you first enter the folder:
#
#     cd 17_virtual_py
#
# then you only need:
#
#     source venv/bin/activate


# ============================================================
# 9. HOW TO CHECK WHETHER venv IS ACTIVE
# ============================================================

# The easiest method:
#
# Look at the terminal prompt.
#
# Example:
#
#     (venv) username@MacBook project %
#
# "(venv)" means active.
#
#
# You can also run:
#
#     which python3
#
# If the environment is active, it should point somewhere
# inside your project's venv.
#
# Example:
#
#     /Users/username/project/venv/bin/python3
#
#
# Another reliable check:
#
#     python3 -c "import sys; print(sys.executable)"
#
# It should show the Python executable inside venv.


# ============================================================
# 10. CHECK PYTHON VERSION
# ============================================================

# Run:
#
#     python3 --version
#
# Example:
#
#     Python 3.12.7
#
#
# You can also use:
#
#     python --version
#
# depending on your shell configuration.


# ============================================================
# 11. CHECK pip
# ============================================================

# Recommended:
#
#     python3 -m pip --version
#
#
# When venv is active, pip should point inside the venv.
#
# Example:
#
#     .../project/venv/lib/python3.12/site-packages/pip
#
#
# Using:
#
#     python3 -m pip
#
# is generally safer than relying on a separate "pip"
# command because it explicitly uses that Python interpreter.


# ============================================================
# 12. INSTALL PACKAGES INSIDE VENV
# ============================================================

# Activate venv first:
#
#     source venv/bin/activate
#
#
# Then:
#
#     python3 -m pip install requests
#
#
# Or:
#
#     python3 -m pip install numpy pandas
#
#
# These packages are installed into the virtual environment,
# not your normal global Python environment.


# ============================================================
# 13. CHECK INSTALLED PACKAGES
# ============================================================

# Run:
#
#     python3 -m pip list
#
#
# Or:
#
#     python3 -m pip freeze
#
#
# "pip list" gives a readable list.
#
# "pip freeze" is commonly used to generate dependency
# information.


# ============================================================
# 14. requirements.txt
# ============================================================

# A project commonly stores its dependencies in:
#
#     requirements.txt
#
#
# Example:
#
#     requests==2.32.4
#     numpy==2.3.2
#     pandas==2.3.1
#
#
# Generate it using:
#
#     python3 -m pip freeze > requirements.txt
#
#
# Install everything from it using:
#
#     python3 -m pip install -r requirements.txt


# ============================================================
# 15. DEACTIVATE VIRTUAL ENVIRONMENT
# ============================================================

# When you are finished:
#
#     deactivate
#
#
# The "(venv)" should disappear from the terminal prompt.
#
#
# IMPORTANT:
#
# You do NOT need to delete the venv after every use.
#
# You normally:
#
#     activate → work → deactivate
#
# and later:
#
#     activate → work → deactivate


# ============================================================
# 16. DO WE NEED TO CREATE venv EVERY TIME?
# ============================================================

# NO.
#
# You create the environment once.
#
# Example:
#
#     python3 -m venv venv
#
# Then whenever you return to the project:
#
#     source venv/bin/activate
#
#
# You only create a new venv if:
#
# - The old environment is deleted
# - The environment is corrupted
# - You intentionally want a fresh environment
# - You need a different Python setup


# ============================================================
# 17. DO WE COMMIT venv TO GIT?
# ============================================================

# NO.
#
# The venv directory should normally NOT be committed
# to Git.
#
# Add this to .gitignore:
#
#     venv/
#
# or:
#
#     .venv/
#
#
# Why?
#
# Virtual environments can contain many files and are
# machine-specific.
#
# Instead, commit:
#
#     requirements.txt
#
# so another developer can recreate the environment.


# ============================================================
# 18. .venv vs venv
# ============================================================

# Both are valid names.
#
# Common choices:
#
#     venv/
#
# or:
#
#     .venv/
#
#
# ".venv" is popular because it is hidden by default
# in many file explorers.
#
# Example:
#
#     project/
#     ├── .venv/
#     ├── src/
#     ├── requirements.txt
#     └── README.md
#
#
# If using .venv:
#
#     python3 -m venv .venv
#
# Activate:
#
#     source .venv/bin/activate


# ============================================================
# 19. YOUR CURRENT PROJECT
# ============================================================

# Your current structure is approximately:
#
#     MPython/
#     │
#     ├── 01_basics/
#     ├── 02_list/
#     ├── 03_tuples/
#     ├── ...
#     ├── 16_mongodb_py/
#     │
#     └── 17_virtual_py/
#         ├── theory/
#         │   └── 01_intro.py
#         │
#         └── venv/
#
#
# Since your venv is inside 17_virtual_py:
#
# From MPython:
#
#     source 17_virtual_py/venv/bin/activate
#
#
# Or:
#
#     cd 17_virtual_py
#     source venv/bin/activate


# ============================================================
# 20. WHY DOES "python: aliased to python3" APPEAR?
# ============================================================

# On your Mac, you have configured:
#
#     python -> python3
#
#
# Therefore when you run:
#
#     which python
#
# your shell may display:
#
#     python: aliased to python3
#
#
# This is NOT an error.
#
# It simply means your shell has an alias:
#
#     python = python3
#
#
# You can check it using:
#
#     type python
#
#
# If you see:
#
#     python is an alias for python3
#
# everything is working as configured.


# ============================================================
# 21. IMPORTANT: ALIAS vs VIRTUAL ENVIRONMENT
# ============================================================

# These are two different concepts.
#
#
# ALIAS:
#
#     python -> python3
#
# This controls what command your shell executes.
#
#
# VIRTUAL ENVIRONMENT:
#
#     project/venv/bin/python3
#
# This provides an isolated Python environment.
#
#
# So:
#
#     "python: aliased to python3"
#
# does NOT mean your venv is broken.


# ============================================================
# 22. PYTHON MODULE venv vs PACKAGE virtualenv
# ============================================================

# There are two related things:
#
#
# 1. venv
#
# Built into modern Python.
#
# Create environment:
#
#     python3 -m venv venv
#
#
# 2. virtualenv
#
# A third-party tool/package.
#
# Historically it was commonly used to create environments.
#
# Installation:
#
#     python3 -m pip install virtualenv
#
#
# Then:
#
#     virtualenv venv
#
#
# For normal projects, you usually do NOT need virtualenv.
#
# Python's built-in venv is sufficient for many projects.


# ============================================================
# 23. WHEN SHOULD YOU USE A VIRTUAL ENVIRONMENT?
# ============================================================

# Use a virtual environment when working on a real Python
# project that has external dependencies.
#
# Examples:
#
#     FastAPI project
#     Django project
#     Flask project
#     Machine Learning project
#     Data Science project
#     Automation project
#     Web scraping project
#     AI/ML project
#
#
# For a tiny Python file:
#
#     hello.py
#
# you don't necessarily need one.


# ============================================================
# 24. AI / ML PROJECT EXAMPLE
# ============================================================

# Imagine:
#
#     Project A
#
# needs:
#
#     numpy
#     pandas
#     scikit-learn
#     torch
#
#
# You create:
#
#     python3 -m venv .venv
#
# Activate:
#
#     source .venv/bin/activate
#
# Install:
#
#     python3 -m pip install numpy pandas scikit-learn torch
#
#
# Now these dependencies belong to this project environment.


# ============================================================
# 25. REAL COMPANY PROJECT WORKFLOW
# ============================================================

# A typical Python project can look like:
#
#     my-project/
#     │
#     ├── .venv/              # Local environment
#     ├── src/
#     ├── tests/
#     ├── .gitignore
#     ├── requirements.txt
#     ├── README.md
#     └── pyproject.toml
#
#
# Developer:
#
#     python3 -m venv .venv
#
#     source .venv/bin/activate
#
#     python3 -m pip install -r requirements.txt
#
#     python3 src/main.py
#
#
# The ".venv" folder is usually not pushed to Git.


# ============================================================
# 26. VIRTUAL ENVIRONMENT IS NOT A CONTAINER
# ============================================================

# Important distinction:
#
#
# Virtual Environment:
#
#     isolates Python packages and Python environment.
#
#
# Docker:
#
#     isolates an application and its operating environment
#     using containers.
#
#
# Virtual environment:
#
#     Python-level isolation
#
# Docker:
#
#     Application/system-level isolation
#
#
# They solve different problems.


# ============================================================
# 27. VIRTUAL ENVIRONMENT IS NOT A PYTHON VERSION MANAGER
# ============================================================

# A venv does not primarily manage multiple Python versions.
#
# Tools such as:
#
#     pyenv
#
# are commonly used when you need to manage multiple Python
# versions.
#
# Example:
#
#     Python 3.10
#     Python 3.11
#     Python 3.12
#
#
# Then a virtual environment can be created using the
# desired Python interpreter.


# ============================================================
# 28. COMPLETE macOS WORKFLOW
# ============================================================

# Suppose you create a new project:
#
#     mkdir my_project
#     cd my_project
#
#
# Create environment:
#
#     python3 -m venv .venv
#
#
# Activate:
#
#     source .venv/bin/activate
#
#
# Verify:
#
#     which python3
#
#     python3 --version
#
#     python3 -m pip --version
#
#
# Install packages:
#
#     python3 -m pip install requests
#
#
# Save dependencies:
#
#     python3 -m pip freeze > requirements.txt
#
#
# Work:
#
#     python3 app.py
#
#
# Leave environment:
#
#     deactivate


# ============================================================
# 29. NEW MACHINE / NEW DEVELOPER WORKFLOW
# ============================================================

# Suppose someone clones your GitHub project:
#
#     git clone <repository>
#
#     cd project
#
#
# The .venv directory is NOT present because it was ignored.
#
# They create a new one:
#
#     python3 -m venv .venv
#
#
# Activate:
#
#     source .venv/bin/activate
#
#
# Install dependencies:
#
#     python3 -m pip install -r requirements.txt
#
#
# Now they have an environment equivalent to the project's
# required dependencies.


# ============================================================
# 30. COMMON COMMAND CHEAT SHEET — macOS
# ============================================================

# CREATE:
#
#     python3 -m venv venv
#
#
# OR:
#
#     python3 -m venv .venv
#
#
# ACTIVATE:
#
#     source venv/bin/activate
#
#
# IF USING .venv:
#
#     source .venv/bin/activate
#
#
# CHECK PYTHON:
#
#     which python3
#
#
# CHECK EXECUTABLE:
#
#     python3 -c "import sys; print(sys.executable)"
#
#
# CHECK VERSION:
#
#     python3 --version
#
#
# CHECK PIP:
#
#     python3 -m pip --version
#
#
# INSTALL:
#
#     python3 -m pip install package_name
#
#
# LIST:
#
#     python3 -m pip list
#
#
# FREEZE:
#
#     python3 -m pip freeze
#
#
# REQUIREMENTS:
#
#     python3 -m pip freeze > requirements.txt
#
#
# INSTALL REQUIREMENTS:
#
#     python3 -m pip install -r requirements.txt
#
#
# DEACTIVATE:
#
#     deactivate


# ============================================================
# 31. WHAT SHOULD YOU REMEMBER FOR INTERVIEWS?
# ============================================================

# Interview answer:
#
# "A Python virtual environment is an isolated environment
# that allows a project to maintain its own Python packages
# and dependency versions without affecting other projects
# or the global Python installation."
#
#
# Key benefits:
#
# 1. Dependency isolation
# 2. Version management
# 3. Reproducibility
# 4. Avoids dependency conflicts
# 5. Keeps the global Python environment clean


# ============================================================
# 32. DO COMPANIES USE VIRTUAL ENVIRONMENTS?
# ============================================================

# YES.
#
# Python virtual environments are widely used in real-world
# Python development.
#
# However, companies may use different tools depending on
# the project.
#
# Common approaches include:
#
#     venv
#     virtualenv
#     Poetry
#     uv
#     Conda
#     Docker
#
#
# The important concept is:
#
#     isolated + reproducible dependencies
#
# not simply the specific tool used.


# ============================================================
# 33. BASIC vs PROFESSIONAL PYTHON ENVIRONMENT MANAGEMENT
# ============================================================

# BASIC:
#
#     python3 -m venv .venv
#
#     source .venv/bin/activate
#
#     python3 -m pip install requests
#
#
# PROFESSIONAL PROJECTS MAY ALSO USE:
#
#     pyproject.toml
#     Poetry
#     uv
#     pip-tools
#     Conda
#     Docker
#
#
# You don't need to learn all of these immediately.
#
# First understand:
#
#     Python
#     venv
#     pip
#     requirements.txt
#     Git
#
# very well.


# ============================================================
# 34. MOST IMPORTANT MENTAL MODEL
# ============================================================

# Remember this:
#
#
#     PROJECT
#        |
#        └── .venv
#              |
#              ├── Python interpreter
#              ├── pip
#              └── project dependencies
#
#
# GitHub stores:
#
#     source code
#     requirements
#     configuration
#
#
# GitHub normally DOES NOT store:
#
#     .venv/
#
#
# When another developer gets the project:
#
#     create .venv
#          ↓
#     activate .venv
#          ↓
#     install dependencies
#          ↓
#     run project


# ============================================================
# 35. FINAL RULE TO REMEMBER
# ============================================================

# NEW PROJECT:
#
#     python3 -m venv .venv
#
#
# EVERY TIME YOU OPEN THE PROJECT:
#
#     source .venv/bin/activate
#
#
# INSTALL PACKAGES:
#
#     python3 -m pip install <package>
#
#
# FINISHED WORK:
#
#     deactivate
#
#
# DO NOT PUSH:
#
#     .venv/
#
#
# DO PUSH:
#
#     requirements.txt


