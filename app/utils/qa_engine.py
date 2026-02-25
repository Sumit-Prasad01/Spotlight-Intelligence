import requests

from app.common.logger import get_logger
from app.common.custom_exception import CustomException
from app.config.config import Config

logger = get_logger(__name__)


class QAEngine:

    def __init__(self):
        self.api_key = Config.api_key
        self.api_url = Config.api_url
        self.model = Config.chat_model

    def ask_about_celebrity(self, name: str, question: str):
        try:

            if not name:
                return "Please detect a celebrity first."

            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }

            prompt = f"""
You are an expert AI assistant with deep knowledge about celebrities.

The user is asking about: {name}

Answer the following question concisely and accurately.

Question: {question}
"""

            payload = {
                "model": self.model,
                "messages": [
                    {
                        "role": "system",
                        "content": "You are a knowledgeable and concise celebrity expert."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "temperature": 0.3,
                "max_tokens": 400
            }

            response = requests.post(
                self.api_url,
                headers=headers,
                json=payload
            )

            if response.status_code == 200:
                return response.json()["choices"][0]["message"]["content"]

            logger.error(f"Chat API error: {response.text}")
            return "Sorry, I couldn't find the answer."

        except Exception as e:
            logger.error(f"Error while generating answer: {e}")
            raise CustomException("Failed to answer user question:", e)