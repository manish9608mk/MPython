'''
chatbot.py

This is the main application file.

Responsibilities:
- Take input from the user.
- Validate user input.
- Handle exit commands.
- Send the user's message to Gemini.
- Display Gemini's response.
- Handle API and other errors.

Flow:
User Input
    ↓
Validate Input
    ↓
Send to Gemini
    ↓
Display Response
'''

'''
client.py

This file is responsible for connecting our application to Gemini.

Responsibilities:
- Create the Gemini client.
- Use the API key from config.py.
- Create a chat session with the selected Gemini model.

Flow:
API Key + Model
      ↓
Gemini Client
      ↓
Chat Session
      ↓
Used by chatbot.py
'''


'''
config.py

This file contains application configuration.

Responsibilities:
- Load environment variables from .env.
- Read the Gemini API key.
- Define the Gemini model name.
- Check whether the API key exists.

Important:
The API key is stored in .env,
not directly inside the Python code.

Flow:
.env
 ↓
load_dotenv()
 ↓
GEMINI_API_KEY
 ↓
client.py
'''

'''
Remember the whole architecture like this:
                 .env
                  │
                  ▼
             config.py
          API Key + Model
                  │
                  ▼
             client.py
          Gemini Connection
                  │
                  ▼
            chatbot.py
       User ↔ Gemini Conversation

       
config.py → What configuration do I need?
client.py → How do I connect to Gemini?
chatbot.py → What does my application do?      
'''