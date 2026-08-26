"""
                 GIT + GITHUB CHEAT SHEET


GIT
---
Git = Version Control System
GitHub = Remote hosting platform for Git repositories


1. SETUP
--------

git --version

git config --global user.name "Your Name"
git config --global user.email "your@email.com"

git config --list


2. CREATE REPOSITORY
--------------------

git init


3. CHECK STATUS
---------------

git status


4. SEE CHANGES
--------------

git diff
git diff --staged


5. STAGING
----------

git add file.py
git add .
git add -A

Unstage:

git restore --staged file.py


6. COMMIT
---------

git commit -m "Add feature"


7. HISTORY
----------

git log
git log --oneline
git log --oneline --graph --all

git show
git show <commit-id>


8. GITHUB REMOTE
----------------

git remote -v

git remote add origin <github-url>

git remote remove origin

git remote show origin


9. PUSH
--------

git push

First push:

git push -u origin main

Verbose push:

git push -v origin main


10. CLONE
---------

git clone <github-url>


11. FETCH / PULL
----------------

git fetch

git pull


fetch = download remote information
pull  = fetch + integrate changes


12. BRANCHES
------------

git branch

git branch -a

git branch feature-login

git switch feature-login

Create + switch:

git switch -c feature-login

Switch:

git switch main

Delete:

git branch -d feature-login


13. MERGE
---------

git switch main

git merge feature-login


14. STASH
---------

git stash

git stash list

git stash pop

git stash apply

git stash drop


15. UNDO
--------

Discard working-directory changes:

git restore file.py

Unstage:

git restore --staged file.py

Undo latest commit but keep changes:

git reset --soft HEAD~1

Undo commit + unstage:

git reset --mixed HEAD~1

Dangerous:

git reset --hard HEAD~1


16. REVERT
----------

git revert <commit-id>

Safer for already-pushed commits.


17. TAGS
--------

git tag v1.0.0

git tag

git push origin v1.0.0

git push --tags


18. OTHER USEFUL COMMANDS
-------------------------

git blame file.py

git diff main..feature

git log --grep="keyword"

git mv old.py new.py

git rm file.py


=========================================================
              DAILY DEVELOPMENT WORKFLOW
=========================================================

git pull

# Work on code

git status

git add .

git commit -m "Describe the change"

git push


=========================================================
              PROFESSIONAL WORKFLOW

main
 ↓
git pull
 ↓
git switch -c feature/my-feature
 ↓
Write code
 ↓
Run tests
 ↓
git status
 ↓
git add .
 ↓
git commit -m "Add my feature"
 ↓
git push -u origin feature/my-feature
 ↓
Pull Request
 ↓
Code Review
 ↓
CI/CD
 ↓
Merge into main


=========================================================
                 MOST IMPORTANT

git status
git add .
git commit -m "message"
git pull
git push

Remember:

Working Directory
       ↓ git add
Staging Area
       ↓ git commit
Local Repository
       ↓ git push
GitHub
"""