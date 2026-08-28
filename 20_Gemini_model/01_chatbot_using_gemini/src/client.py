from google import genai

from config import GEMINI_API_KEY, MODEL_NAME


client = genai.Client(
    api_key=GEMINI_API_KEY
)


def create_chat(history=None):

    if history is None:
        history = []

    return client.chats.create(
        model=MODEL_NAME,
        history=history,
    )