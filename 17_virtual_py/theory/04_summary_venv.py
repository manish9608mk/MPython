'''
- Python Virtual Environment + Package Management — Final Summary

Whenever I work on a Python project, I should use a virtual environment
for that project.

PROJECT
│
├── .venv/                  → Isolated Python environment
├── src/                    → My Python source code
├── requirements.txt        → List of project dependencies
├── .gitignore              → Files/folders Git should ignore
└── README.md               → Project documentation


1. Create a virtual environment

python3 -m venv .venv


2. Activate it

source .venv/bin/activate


3. Install any Python package I need

pip install django
pip install pymongo

I can install packages according to my project's requirements.


4. Remove a package if I don't need it

pip uninstall pymongo


5. Save all currently installed packages

pip freeze > requirements.txt

This updates requirements.txt with the installed packages and versions.


6. Write my Python code

I can keep my Python source code inside the src/ folder.

Note: src/ is a project-organization convention; Python does not require it.


7. Push the project to GitHub

I can safely push my source code, requirements.txt, README.md, etc.

I should NOT push .venv/ because the virtual environment is
machine-specific and can be recreated.


8. Run the project on another machine

Create a new virtual environment:

python3 -m venv .venv

Activate it:

source .venv/bin/activate

Install all project dependencies:

pip install -r requirements.txt

Now the required packages are installed in the new machine's
virtual environment, and the project can be run.


- Complete Workflow

Create environment
        ↓
Activate environment
        ↓
Install required packages
        ↓
Write code
        ↓
pip freeze > requirements.txt
        ↓
Push project to GitHub
        ↓
Another machine clones the project
        ↓
Create a new .venv
        ↓
Activate .venv
        ↓
pip install -r requirements.txt
        ↓
Run the project


- One-Line Memory Trick

.venv               = Isolated Python environment
pip                 = Package manager
requirements.txt    = Dependency list
pip install         = Install a package
pip uninstall       = Remove a package
pip freeze          = Installed packages → requirements.txt
pip install -r      = requirements.txt → Installed packages
src/                = Source code
.gitignore          = Files Git should not track


- Most Important Rule

DO NOT push .venv/
DO push requirements.txt

The virtual environment can always be recreated from
requirements.txt.

'''