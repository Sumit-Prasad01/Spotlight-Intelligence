import base64
import json
import requests

from app.common.custom_exception import CustomException
from app.common.logger import get_logger
from app.config.config import Config

logger = get_logger(__name__)


class CelebrityDetector:

    def __init__(self):
        self.api_key = Config.api_key
        self.api_url = Config.api_url
        self.model = Config.image_model

    def identify(self, image_bytes):
        try:
            # Encode image
            encoded_image = base64.b64encode(image_bytes).decode()

            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }

            payload = {
                "model": self.model,
                "messages": [
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": """
You are a celebrity recognition expert AI.

Identify the person in the image.

Respond ONLY in strict JSON format:

{
  "full_name": "",
  "profession": "",
  "nationality": "",
  "famous_for": "",
  "top_achievements": ""
}

If unknown, respond with:

{
  "full_name": "Unknown"
}

Do not return markdown.
Do not add explanations.
Return valid JSON only.
"""
                            },
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{encoded_image}"
                                }
                            }
                        ]
                    }
                ],
                "temperature": 0,
                "max_tokens": 512
            }

            response = requests.post(
                self.api_url,
                headers=headers,
                json=payload
            )

            if response.status_code != 200:
                logger.error(f"LLM API Error: {response.text}")
                return {"full_name": "Unknown"}, "Unknown"

            raw_content = response.json()["choices"][0]["message"]["content"]

            # Parse JSON safely
            try:
                data = json.loads(raw_content)
            except json.JSONDecodeError:
                logger.error("Invalid JSON returned by model.")
                return {"full_name": "Unknown"}, "Unknown"

            name = data.get("full_name", "Unknown")

            logger.info("Celebrity identification successful.")

            return data, name

        except Exception as e:
            logger.error(f"Error while generating response: {e}")
            raise CustomException("Failed to generate response", e)