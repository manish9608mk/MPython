'''
NEW PYTHON PROJECT — STANDARD SETUP

mkdir my_project
cd my_project
python3 -m venv .venv
source .venv/bin/activate
'''


'''
NEW PYTHON PROJECT — STANDARD SETUP

1. Create a project folder

   mkdir my_project
   cd my_project


2. Create a virtual environment

   python3 -m venv .venv


3. Activate the virtual environment

   source .venv/bin/activate


4. Check that the virtual environment is active

   which python
   python --version
   pip --version

   `which python` should show:
   `.venv/bin/python`


5. Open the current project in VS Code

   code .


6. Create your Python files/folders

   my_project/
   ├── .venv/
   ├── src/
   │   └── main.py
   ├── .gitignore
   └── README.md


7. Add the following to `.gitignore`

   .venv/
   .env
   __pycache__/
   *.pyc


8. Install packages when needed

   pip install package_name

   Example:

   pip install requests


9. Save installed packages

   pip freeze > requirements.txt


10. Run your Python code

    python src/main.py


11. When you finish working, you can deactivate the virtual environment

    deactivate


12. When you return to the same project later

    cd my_project
    source .venv/bin/activate

    Then continue working.


IMPORTANT:

.venv               → Python virtual environment
.env                → Secrets / environment variables
src/                → Actual Python source code
requirements.txt    → Project dependencies
.gitignore          → Files that should not be pushed to GitHub
README.md           → Project documentation


RULE:

New project → Create a new `.venv`

Same project → Reuse the same `.venv`

Do NOT create a new `.venv` every time you open the project.
'''