'''
important thing you just learned:

Python
 │
 ├── imports
 ├── modules
 ├── functions
 ├── variables
 ├── environment variables
 ├── .env
 ├── virtual environment
 ├── exception handling
 ├── loops
 ├── conditions
 ├── classes/objects through SDK
 ├── API
 ├── HTTP/network communication
 ├── external SDK
 └── modular project structure

------------------------------
And importantly, I didn't just make an API call—I've already introduced several real
software-engineering concepts:
virtual environments
environment variables
secret management
.gitignore
dependency management
modules
imports
configuration separation
API clients
chat sessions
exception handling
HTTP/API error handling
project structure

-------------------------------
 .env
→ SECRET

config.py
→ CONFIGURATION

client.py
→ GEMINI CONNECTION

chatbot.py
→ APPLICATION LOGIC

requirements.txt
→ DEPENDENCIES

.gitignore
→ FILES TO IGNORE

.venv
→ ISOLATED PYTHON ENVIRONMENT

__init__.py
→ src PACKAGE

-----------------------------------

important architecture:
                    .env
                     │
                     │ GEMINI_API_KEY
                     ↓
                 config.py
                     │
             ┌───────┴───────┐
             │               │
     GEMINI_API_KEY      MODEL_NAME
             │               │
             └───────┬───────┘
                     ↓
                 client.py
                     │
                     ↓
              genai.Client()
                     │
                     ↓
              client.chats.create()
                     │
                     ↓
                    chat
                     │
                     ↓
                chatbot.py
                     │
                     ↓
              input("You: ")
                     │
                     ↓
             chat.send_message()
                     │
                     ↓
                 Gemini API
                     │
                     ↓
                 response
                     │
                     ↓
              response.text
                     │
                     ↓
              print("Gemini")
 '''