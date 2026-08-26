"""
                GIT & GITHUB

Goal:
    Understand Git + GitHub well enough to:
    1. Work on personal projects
    2. Maintain projects professionally
    3. Collaborate with a team
    4. Work with branches and pull requests
    5. Handle conflicts
    6. Understand common company workflows
    7. Safely manage code on GitHub

============================================================
1. WHAT IS GIT?
============================================================

Git is a distributed version control system.

It tracks changes in our source code.

Example:

Without Git:

    project/
        app.py

You change app.py many times.

You may lose track of:
    - what changed
    - when it changed
    - why it changed
    - who changed it

With Git:

    Version 1
       ↓
    Version 2
       ↓
    Version 3
       ↓
    Version 4

Git keeps a history of these changes.

============================================================
2. WHAT IS GITHUB?
============================================================

Git and GitHub are NOT the same thing.

Git
    → Version control system
    → Runs locally on our computer

GitHub
    → Cloud platform for hosting Git repositories
    → Used for collaboration
    → Pull Requests
    → Code Reviews
    → Issues
    → CI/CD through GitHub Actions
    → Team collaboration

Simple analogy:

    Git      = Tool
    GitHub   = Online platform that hosts Git repositories

============================================================
3. GIT vs GITHUB
============================================================

Git:

    Your Mac
       |
       └── Git
            |
            └── Local repository

GitHub:

    Internet
       |
       └── GitHub
            |
            └── Remote repository

Git can work without GitHub.

GitHub normally uses Git underneath.

============================================================
4. IMPORTANT GIT TERMINOLOGY
============================================================

Repository
    A project tracked by Git.

Working Directory
    The actual files you are currently editing.

Staging Area
    Changes selected for the next commit.

Commit
    A saved snapshot of changes.

Branch
    An independent line of development.

Remote
    A remote Git repository, usually GitHub.

origin
    Default name commonly given to the GitHub remote.

HEAD
    Represents the currently checked-out commit/branch position.

Clone
    Copy a remote repository to your local machine.

Fetch
    Download remote changes without changing your current files.

Pull
    Fetch + integrate remote changes into your current branch.

Push
    Upload local commits to the remote repository.

Merge
    Combine changes from one branch into another.

Rebase
    Reapply commits on top of another branch.

Pull Request
    Request to merge your branch into another branch on GitHub.

============================================================
5. THE BASIC GIT FLOW
============================================================

The most important workflow:

    Edit files
        ↓
    git status
        ↓
    git add
        ↓
    git commit
        ↓
    git push
        ↓
    GitHub

Example:

    Modify app.py

    git status

    git add app.py

    git commit -m "Add login functionality"

    git push

============================================================
6. CHECK WHETHER GIT IS INSTALLED
============================================================

git --version

Example:

    git version 2.x.x

============================================================
7. CONFIGURE GIT
============================================================

Set username:

git config --global user.name "Your Name"

Set email:

git config --global user.email "your@email.com"

Check configuration:

git config --global --list

Check a specific value:

git config user.name
git config user.email

============================================================
8. CREATE A NEW GIT REPOSITORY
============================================================

Go inside your project:

cd my-project

Initialize Git:

git init

This creates:

    .git/

The .git directory contains Git's internal repository data.

IMPORTANT:

    Do NOT manually modify .git.

============================================================
9. CHECK REPOSITORY STATUS
============================================================

git status

This is one of the MOST IMPORTANT commands.

It tells you:

    - current branch
    - modified files
    - staged files
    - untracked files
    - commits ahead/behind remote

Use it frequently.

============================================================
10. GIT ADD
============================================================

Stage one file:

git add app.py

Stage multiple files:

git add app.py config.py

Stage everything:

git add .

Meaning:

    Working Directory
          ↓
       git add
          ↓
    Staging Area

IMPORTANT:

git add does NOT create a commit.

It only prepares changes for the next commit.

============================================================
11. GIT COMMIT
============================================================

Create a commit:

git commit -m "Add user authentication"

A commit is a snapshot of staged changes.

Flow:

    Working Directory
          ↓
       git add
          ↓
    Staging Area
          ↓
      git commit
          ↓
    Local Repository

Good commit message:

git commit -m "Add user authentication"

Bad:

git commit -m "changes"

Better commit messages explain WHAT changed.

============================================================
12. VIEW COMMIT HISTORY
============================================================

Basic:

git log

Compact:

git log --oneline

Graph:

git log --oneline --graph --all

Example:

    a1b2c3d Add authentication
    9f8e7d6 Add database connection
    3c2b1a0 Initial project

============================================================
13. GIT DIFF
============================================================

See unstaged changes:

git diff

See staged changes:

git diff --staged

Purpose:

    Understand exactly what changed
    BEFORE committing.

Professional habit:

    git diff
    git status
    git add
    git diff --staged
    git commit

============================================================
14. GITIGNORE
============================================================

.gitignore tells Git which files/folders should NOT be tracked.

Example:

    .venv/
    __pycache__/
    .env
    *.pyc
    .DS_Store

Typical Python .gitignore:

    .venv/
    __pycache__/
    *.pyc
    .env
    .pytest_cache/

IMPORTANT:

Never commit secrets such as:

    API keys
    passwords
    AWS credentials
    database passwords
    private keys
    .env files containing secrets

============================================================
15. CONNECT LOCAL REPOSITORY TO GITHUB
============================================================

Create a repository on GitHub.

Then:

git remote add origin https://github.com/USERNAME/REPOSITORY.git

Check:

git remote -v

Example:

origin  https://github.com/user/project.git (fetch)
origin  https://github.com/user/project.git (push)

============================================================
16. PUSH CODE TO GITHUB
============================================================

First push:

git push -u origin main

After upstream is configured:

git push

Meaning:

    Local repository
          ↓
       git push
          ↓
    GitHub repository

============================================================
17. CLONE A GITHUB REPOSITORY
============================================================

To download an existing project:

git clone https://github.com/USERNAME/REPOSITORY.git

Then:

cd REPOSITORY

Example:

git clone https://github.com/user/project.git

============================================================
18. FETCH vs PULL
============================================================

FETCH:

git fetch origin

Downloads remote changes.

It does NOT automatically modify your current branch.

PULL:

git pull

Usually:

    git fetch
        +
    merge/rebase depending on configuration

Simple:

    fetch = download information

    pull = download + integrate

============================================================
19. BRANCHES
============================================================

A branch is an independent line of development.

Example:

                main
                 |
                 A
                 |
                 B
                / \
               /   \
          feature   bugfix
             |        |
             C        D

Main branch:

    main

Feature branch:

    feature/login

============================================================
20. CHECK BRANCHES
============================================================

Current branches:

git branch

All local + remote branches:

git branch -a

============================================================
21. CREATE A BRANCH
============================================================

git branch feature-login

Switch to it:

git switch feature-login

Modern preferred command:

git switch -c feature-login

This:

    creates branch
        +
    switches to it

============================================================
22. BRANCH WORKFLOW
============================================================

Create feature branch:

git switch -c feature-login

Work:

    edit files

Check:

git status

Stage:

git add .

Commit:

git commit -m "Add login functionality"

Push:

git push -u origin feature-login

Now GitHub contains:

    main
    feature-login

============================================================
23. SWITCH BETWEEN BRANCHES
============================================================

git switch main

Switch back:

git switch feature-login

Older command:

git checkout main

Modern Git:

    Prefer git switch for branch switching.

============================================================
24. MERGE
============================================================

Suppose:

    main
      |
      A
      |
      B

feature:

      B
      |
      C
      |
      D

To merge feature into main:

git switch main

git merge feature

Now:

    main
      |
      A
      |
      B
     / \
    C   |
     \ /
      D

============================================================
25. DELETE A BRANCH
============================================================

Local branch:

git branch -d feature-login

Force delete:

git branch -D feature-login

Delete remote branch:

git push origin --delete feature-login

============================================================
26. PULL REQUEST
============================================================

A Pull Request (PR) is a GitHub collaboration mechanism.

Typical workflow:

    Create branch
         ↓
    Write code
         ↓
    Commit
         ↓
    Push branch
         ↓
    Open Pull Request
         ↓
    Code Review
         ↓
    CI/CD checks
         ↓
    Approval
         ↓
    Merge into main

Important:

A Pull Request is primarily a GitHub concept.

Git itself does not have "Pull Requests".

============================================================
27. PROFESSIONAL COMPANY WORKFLOW
============================================================

Suppose you work at a company.

You normally DO NOT directly modify main.

Typical workflow:

                    main
                     |
                     |
              create branch
                     |
                     ↓
              feature/payment
                     |
                 write code
                     |
                  commit
                     |
                   push
                     |
                     ↓
              Pull Request
                     |
              ┌──────┴──────┐
              │             │
          Code Review    CI/CD Tests
              │             │
              └──────┬──────┘
                     ↓
                  Approval
                     ↓
                  Merge
                     ↓
                    main

============================================================
28. WHY COMPANIES USE BRANCHES
============================================================

Imagine 10 developers.

Developer A:

    feature/login

Developer B:

    feature/payment

Developer C:

    bugfix/cart

Developer D:

    feature/search

Everyone can work independently.

Then PRs are created.

This prevents everyone from directly changing main.

============================================================
29. COMMON COMPANY BRANCHES
============================================================

Different companies use different strategies.

Common branches:

    main
    develop
    feature/*
    bugfix/*
    hotfix/*
    release/*

Example:

    main
    develop

    feature/user-login
    feature/payment

    bugfix/cart-total

Not every company uses all of these.

Modern teams often use:

    main
      +
    short-lived feature branches

============================================================
30. BRANCH NAMING
============================================================

Good:

feature/user-login
feature/payment-api
bugfix/cart-total
hotfix/payment-failure

Avoid:

test
abc
mybranch
new
final
final2
final-final

============================================================
31. GIT MERGE CONFLICT
============================================================

A conflict happens when Git cannot automatically combine changes.

Example:

Developer A:

    print("Hello")

Developer B:

    print("Hi")

Both modify the same part of a file.

Git may produce:

<<<<<<< HEAD
print("Hello")
=======
print("Hi")
>>>>>>> feature

You must manually decide what the final code should be.

Then:

git add file.py

git commit

If merging a branch:

git merge --continue

============================================================
32. HOW TO HANDLE A MERGE CONFLICT
============================================================

Step 1:

    Read the conflict.

Step 2:

    Decide the correct code.

Step 3:

    Remove conflict markers:

<<<<<<<
=======
>>>>>>>

Step 4:

    Save the file.

Step 5:

git add file.py

Step 6:

git commit

Then continue your workflow.

============================================================
33. GIT STASH
============================================================

Sometimes you have unfinished work.

Example:

You are working on:

    feature/login

But suddenly you need to switch branches.

You don't want to commit unfinished code.

Use:

git stash

Your changes are temporarily stored.

Then:

git switch main

Later:

git switch feature/login

Restore:

git stash pop

Useful commands:

git stash
git stash pop
git stash list
git stash apply
git stash drop

============================================================
34. GIT RESET
============================================================

RESET moves your branch/HEAD to another commit.

Three important modes:

    --soft
    --mixed
    --hard

Example:

git reset --soft HEAD~1

Removes the last commit but keeps changes staged.

------------------------------------------------------------

git reset HEAD~1

Default is mixed.

Removes the commit and unstages changes.

Files remain modified.

------------------------------------------------------------

git reset --hard HEAD~1

Removes commit AND changes.

DANGEROUS.

Do NOT use --hard casually.

============================================================
35. GIT REVERT
============================================================

git revert creates a NEW commit that reverses an earlier commit.

Example:

    A → B → C

Revert C:

    A → B → C → D

D reverses C.

This is generally safer for shared branches.

Important:

    reset = move history

    revert = create a new reversing commit

For public/shared branches, prefer revert when undoing already-pushed changes.

============================================================
36. GIT REBASE
============================================================

Rebase moves/replays commits onto another base.

Example:

Before:

    main:
        A --- B

    feature:
        A --- B --- C --- D

If main gets:

        A --- B --- E

Rebase feature:

        A --- B --- E --- C' --- D'

Rebase creates new commit identities.

Basic command:

git switch feature

git rebase main

IMPORTANT:

Avoid rebasing shared/public branches without understanding the consequences.

============================================================
37. MERGE vs REBASE
============================================================

MERGE:

    Preserves branch history.

REBASE:

    Creates a more linear history.

Example:

Merge:

    A---B---E
         \   \
          C---D---M

Rebase:

    A---B---E---C'---D'

Both are useful.

Company policy determines which workflow your team uses.

============================================================
38. CHERRY-PICK
============================================================

Apply one specific commit to another branch.

Example:

    main:
    A---B

    feature:
    A---B---C---D

You want only C in main:

git switch main

git cherry-pick <commit-hash>

Result:

    A---B---C'

Useful for:

    hotfixes
    selected changes
    backporting fixes

============================================================
39. TAGS
============================================================

Tags mark important commits.

Example:

v1.0.0
v1.1.0
v2.0.0

Create:

git tag v1.0.0

Push:

git push origin v1.0.0

Push all tags:

git push origin --tags

Used commonly for releases.

============================================================
40. REMOTE COMMANDS
============================================================

List remotes:

git remote -v

Add remote:

git remote add origin URL

Change remote:

git remote set-url origin URL

Remove remote:

git remote remove origin

============================================================
41. CHECK REMOTE BRANCHES
============================================================

git branch -r

All branches:

git branch -a

============================================================
42. GIT SHOW
============================================================

Show details of a commit:

git show <commit-hash>

Example:

git show 49ec6d9

============================================================
43. FIND COMMITS
============================================================

git log --oneline

Search commit messages:

git log --grep="login"

Show recent commits:

git log -5 --oneline

============================================================
44. GIT BLAME
============================================================

git blame app.py

Shows which commit/author last changed each line.

Useful when investigating:

    Who changed this?

    When was this line introduced?

    Which commit changed this behavior?

============================================================
45. GIT CLEAN
============================================================

Shows untracked files that could be removed:

git clean -n

Actually remove untracked files:

git clean -f

Be careful.

============================================================
46. UNSTAGE A FILE
============================================================

If you accidentally run:

git add app.py

You can unstage:

git restore --staged app.py

============================================================
47. DISCARD LOCAL FILE CHANGES
============================================================

Restore a file:

git restore app.py

This discards uncommitted changes in that file.

Be careful.

============================================================
48. GIT DIFF BETWEEN COMMITS
============================================================

git diff commit1 commit2

Example:

git diff HEAD~1 HEAD

Shows changes between the previous commit and current commit.

============================================================
49. COMMON DAILY WORKFLOW
============================================================

Start your day:

git switch main

git pull

Create feature branch:

git switch -c feature/user-profile

Work on code.

Check:

git status

Review changes:

git diff

Stage:

git add .

Review staged changes:

git diff --staged

Commit:

git commit -m "Add user profile API"

Push:

git push -u origin feature/user-profile

Create Pull Request on GitHub.

After approval:

    PR merged

Then update local main:

git switch main

git pull

Delete local feature branch:

git branch -d feature/user-profile

============================================================
50. IMPORTANT COMMAND CHEAT SHEET
============================================================

SETUP
-----

git --version

git config --global user.name "Name"

git config --global user.email "Email"


CREATE
------

git init

git clone URL


STATUS
------

git status

git log

git log --oneline

git diff

git diff --staged


STAGE
-----

git add file.py

git add .


COMMIT
------

git commit -m "message"


REMOTE
------

git remote -v

git remote add origin URL

git fetch

git pull

git push


BRANCH
------

git branch

git branch -a

git switch main

git switch -c feature/name

git branch -d feature/name


MERGE
------

git merge branch-name


REBASE
------

git rebase main


STASH
-----

git stash

git stash pop

git stash list


UNDO
----

git restore file.py

git restore --staged file.py

git reset --soft HEAD~1

git revert <commit>


ADVANCED
--------

git cherry-pick <commit>

git tag v1.0.0

git blame file.py

git show <commit>


============================================================
51. LOCAL vs REMOTE
============================================================

LOCAL:

    Working Directory
          ↓
    Staging Area
          ↓
    Local Repository

REMOTE:

    GitHub Repository

Full picture:

    Working Directory
            │
         git add
            ↓
       Staging Area
            │
       git commit
            ↓
     Local Repository
            │
         git push
            ↓
       GitHub Remote


To get changes:

       GitHub Remote
            │
         git fetch
            ↓
     Local Repository
            │
         merge/rebase
            ↓
     Working Directory


git pull basically combines:

    fetch + integration

============================================================
52. WHAT HAPPENS WHEN I COMMIT?
============================================================

Suppose:

app.py

contains:

    print("Hello")

You modify it:

    print("Hello World")

Then:

git add app.py

The modified version goes into staging.

Then:

git commit -m "Update greeting"

Git creates a new commit.

That commit has:

    commit ID
    author
    timestamp
    parent commit
    snapshot/reference to project state

============================================================
53. WHAT SHOULD BE PUSHED TO GITHUB?
============================================================

Usually push:

    source code
    README.md
    requirements.txt
    Dockerfile
    docker-compose.yml
    configuration templates
    tests
    CI/CD configuration
    documentation

Do NOT push:

    .venv/
    __pycache__/
    *.pyc
    .env
    passwords
    API keys
    private keys
    huge generated files
    machine-specific files

============================================================
54. PYTHON PROJECT + GIT
============================================================

Example:

my-project/
│
├── .git/
├── .gitignore
├── README.md
├── requirements.txt
├── src/
│   ├── main.py
│   ├── database.py
│   └── api.py
│
├── tests/
│   ├── test_api.py
│   └── test_database.py
│
└── .venv/

Git tracks:

    src/
    tests/
    README.md
    requirements.txt
    .gitignore

Git ignores:

    .venv/

============================================================
55. TEAM DEVELOPMENT
============================================================

Imagine a company with 5 developers.

                    GitHub
                       │
                     main
                       │
       ┌───────────────┼────────────────┐
       ↓               ↓                ↓
 feature/login    feature/payment   bugfix/cart
       │               │                │
       ↓               ↓                ↓
      PR              PR               PR
       │               │                │
       └───────────────┼────────────────┘
                       ↓
                  Code Review
                       ↓
                   CI / Tests
                       ↓
                    Approval
                       ↓
                     Merge
                       ↓
                     main

============================================================
56. CODE REVIEW
============================================================

In companies, developers review each other's code.

Reviewer may check:

    - correctness
    - readability
    - security
    - performance
    - tests
    - architecture
    - maintainability
    - coding standards

Example PR:

    Title:
        Add user authentication API

    Description:
        Added login endpoint.
        Added password hashing.
        Added unit tests.

============================================================
57. CI/CD + GITHUB
============================================================

Modern companies often connect GitHub to CI/CD.

Example:

Developer:

    git push
        ↓
    Pull Request
        ↓
    GitHub Actions
        ↓
    Run tests
        ↓
    Run linting
        ↓
    Build application
        ↓
    Security checks
        ↓
    Approval
        ↓
    Merge
        ↓
    Deployment

Git is therefore part of the larger software delivery process.

============================================================
58. GITHUB ACTIONS
============================================================

GitHub Actions can automatically execute workflows.

Example:

    push code
       ↓
    run tests
       ↓
    build Docker image
       ↓
    deploy application

Workflow files are usually stored in:

.github/workflows/

Example:

.github/
└── workflows/
    └── ci.yml

============================================================
59. ISSUES
============================================================

GitHub Issues can track:

    bugs
    features
    tasks
    improvements

Example:

Issue #123

    "Login API returns 500 when password is incorrect"

Developer:

    creates branch
    fixes issue
    creates PR
    links PR to issue
    merges PR

============================================================
60. PROFESSIONAL DEVELOPMENT CYCLE
============================================================

Typical company workflow:

    1. Pick Jira/GitHub issue
              ↓
    2. Create feature branch
              ↓
    3. Write code
              ↓
    4. Write tests
              ↓
    5. git status
              ↓
    6. git diff
              ↓
    7. git add
              ↓
    8. git commit
              ↓
    9. git push
              ↓
   10. Create Pull Request
              ↓
   11. CI checks
              ↓
   12. Code review
              ↓
   13. Fix review comments
              ↓
   14. Push new commits
              ↓
   15. Approval
              ↓
   16. Merge
              ↓
   17. Deployment

============================================================
61. IMPORTANT SECURITY RULES
============================================================

NEVER commit:

    API_KEY=abc123
    PASSWORD=secret
    AWS_SECRET_ACCESS_KEY=...
    private keys
    database credentials

Use:

    .env

and add:

    .env

to .gitignore.

For production:

    use proper secret-management systems.

Examples:

    AWS Secrets Manager
    AWS Systems Manager Parameter Store
    HashiCorp Vault
    GitHub Actions Secrets

============================================================
62. IF YOU ACCIDENTALLY COMMIT A SECRET
============================================================

IMPORTANT:

Deleting the file in a later commit does NOT necessarily mean
the secret is safe.

The secret may still exist in Git history.

Correct response:

    1. Revoke/rotate the secret immediately.
    2. Remove it from the repository/history if necessary.
    3. Update the application with the new secret.
    4. Investigate whether the secret was exposed.

NEVER assume:

    "I deleted the file, so the secret is safe."

============================================================
63. MOST IMPORTANT COMMANDS TO MASTER FIRST
============================================================

Do NOT try to memorize every Git command immediately.

Master these first:

    git status
    git add
    git commit
    git log
    git diff
    git push
    git pull
    git clone
    git fetch
    git branch
    git switch
    git merge
    git stash
    git restore

Then learn:

    rebase
    reset
    revert
    cherry-pick
    tags
    bisect
    reflog

============================================================
64. THE MENTAL MODEL TO REMEMBER
============================================================

LOCAL:

    Edit
      ↓
    git status
      ↓
    git add
      ↓
    Staging
      ↓
    git commit
      ↓
    Local Git history

REMOTE:

    git push
      ↓
    GitHub

GET TEAM CHANGES:

    git pull
      ↓
    Local branch updated

TEAM WORK:

    branch
      ↓
    code
      ↓
    commit
      ↓
    push
      ↓
    Pull Request
      ↓
    Review
      ↓
    CI
      ↓
    Merge
      ↓
    main

============================================================
65. FINAL MEMORY TRICK
============================================================

Git:

    "Track my code history."

GitHub:

    "Host and collaborate on my Git repositories."

git status:

    "What is happening?"

git add:

    "Prepare these changes."

git commit:

    "Save this version."

git push:

    "Send my commits to GitHub."

git pull:

    "Get and integrate the latest remote changes."

git fetch:

    "Download remote information without integrating it."

git clone:

    "Give me a local copy of this repository."

git branch:

    "Show/manage branches."

git switch:

    "Move to another branch."

git merge:

    "Combine branches."

git stash:

    "Temporarily save unfinished work."

git restore:

    "Discard/restore file changes."

git revert:

    "Create a new commit that undoes an old commit."

git rebase:

    "Replay commits onto a new base."

Pull Request:

    "Please review and merge my changes."

"""