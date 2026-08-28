import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-3.7-flash")

# Try current Flash models if the selected one is unavailable.
FALLBACK_MODELS = [
    "gemini-3.7-flash",
    "gemini-3.6-flash",
    "gemini-3.5-flash",
]


class GeminiError(Exception):
    pass


class GeminiChat:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        self.client = None
        self.chat = None
        self.model_name = MODEL_NAME

        if not self.api_key:
            raise GeminiError(
                "GEMINI_API_KEY is missing. Add it to .env and restart Streamlit."
            )

        try:
            self.client = genai.Client(api_key=self.api_key)
        except Exception as exc:
            raise GeminiError(
                "Could not initialize Google Gemini. Run: pip install -U google-genai"
            ) from exc

    def _create_chat(self, model_name, history=None):
        if history:
            from google.genai import types

            sdk_history = []
            for item in history:
                sdk_history.append(
                    types.Content(
                        role="user" if item["role"] == "user" else "model",
                        parts=[types.Part(text=item["content"])],
                    )
                )

            return self.client.chats.create(
                model=model_name,
                history=sdk_history,
            )

        return self.client.chats.create(model=model_name)

    def send(self, message, history=None, existing_chat=None):
        message = message.strip()
        if not message:
            raise GeminiError("Please enter a message.")

        # Reuse current chat first.
        if existing_chat is not None:
            try:
                response = existing_chat.send_message(message=message)
                text = (response.text or "").strip()
                if text:
                    self.chat = existing_chat
                    return text
            except Exception:
                pass

        last_error = None

        for model in FALLBACK_MODELS:
            try:
                chat = self._create_chat(model, history=history)
                response = chat.send_message(message=message)
                text = (response.text or "").strip()

                if not text:
                    raise GeminiError("Gemini returned an empty response.")

                self.chat = chat
                self.model_name = model
                return text

            except Exception as exc:
                last_error = exc

        error_text = str(last_error) if last_error else ""

        if "404" in error_text or "NOT_FOUND" in error_text:
            raise GeminiError(
                "The Gemini model is unavailable for this API key. "
                "The app already tried the current Flash models. "
                "Check your Google AI Studio API key and GEMINI_MODEL in .env."
            ) from last_error

        if "401" in error_text or "403" in error_text:
            raise GeminiError(
                "Gemini rejected the API key. Check GEMINI_API_KEY in .env."
            ) from last_error

        if "429" in error_text or "RESOURCE_EXHAUSTED" in error_text:
            raise GeminiError(
                "Gemini rate limit/quota reached. Wait a little and try again."
            ) from last_error

        raise GeminiError(
            "Gemini request failed. Check your internet connection and API key."
        ) from last_error
