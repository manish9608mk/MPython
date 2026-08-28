# for run in integrated terminal -
# activate virtual py environment: source .venv/bin/activate
# now run actual code files: python src/chatbot.py 
# now we see the result
# ye file nahi chalega because, ismein virtual invironment setup nhi hai 
# 01_chatbot_using_gemini.py mein chalega but, iss file mein bhi chala sakte hain 
# .venv and requirement.txt ka use karke 


'''
#1
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

chat = client.chats.create(
    model="gemini-3.6-flash"
)

while True:

    print("-" * 60)

    user_input = input("You: ")

    # Exit conditions
    if user_input.lower().strip() in ["exit", "bye", "stop", "break"]:
        print("Gemini: Goodbye!")
        break

    try:
        response = chat.send_message(
            user_input
        )

        print("\nGemini:", response.text)

    except Exception as e:
        print("\nError:", e)
'''



'''
01_chatbot_using_gemini/
│
├── .env                 ← API key 🔐
├── .gitignore           ← protect .env from Git
├── requirements.txt     ← dependencies
├── .venv/               ← virtual environment
│
└── src/
    └── chatbot.py       ← actual application code 🚀

    
.env → secret
config.py → configuration
client.py → Gemini client
chatbot.py → application logic


Phase 1
Basic Gemini API
       ↓
Phase 2
User input loop
       ↓
Phase 3
Conversation history / memory
       ↓
Phase 4
Error handling
       ↓
Phase 5
Clean project structure
       ↓
Phase 6
Streamlit UI
       ↓
Phase 7
Deploy



                .env
                 │
                 ▼
             config.py
                 │
           API_KEY + MODEL
                 │
                 ▼
              client.py
                 │
          Gemini Chat Client
                 │
                 ▼
             chatbot.py
                 │
        ┌────────┴────────┐
        ▼                 ▼
     User Input       Gemini Response
        │                 │
        └─────── Chat ────┘
'''

