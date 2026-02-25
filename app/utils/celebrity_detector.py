import os
import base64
import requests

from app.common.custom_exception import CustomException
from app.common.logger import get_logger
from app.config.config import Config

logger = get_logger(__name__)

class CelebrityDetector:

    def __init__(self):
        
        self.api_key = Config.api_key
        self.api_url = Config.api_url
        self.model = Config.model
        

    def identify(self, image_bytes):
        try:

            encoded_image = base64.b64encode(image_bytes).decode()

            headers = {
                "Authorization" : f"Bearer {self.api_key}",
                "Content-Type" : "application/json"
            }

            prompt = {
                "model": self.model,
                "messages": [
                    {
                        "role": "user", 
                        "content": [
                            {
                                "type": "text",
                                "text": """You are a celebrity recognition expert AI. 
                                Identify the person in the image. If known, respond in this format:

                                - **Full Name**:
                                - **Profession**:
                                - **Nationality**:
                                - **Famous For**:
                                - **Top Achievements**:

                                If unknown, return "Unknown".
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
                "temperature": 0.3,    
                "max_tokens": 1024     
            }
        
            response = requests.post(self.api_url, headers = headers, json = prompt)

            if response.status_code == 200:
                result = response.json()['choices'][0]['message']['content']

                name = self.extract_name(result)

                return result, name
            
            logger.info(f"Successfully got response from LLM.")
            
            return "Unknown", ""
        
        except Exception as e:
            logger.error(f"Error while generating response : {e}")
            raise CustomException("Failed to generate response : ", e)
        
    
    def extract_names(self, content):
        try:

            for line in content.splitlines():
                if line.lower().startswith("- **full name**:"):
                    return line.split(":")[1].strip()
            logger.info(f"Names fetched successfully.")
            
            return "unknown"

        except Exception as e:
            logger.error(f"Error while extracting names : {e}")
            raise CustomException("Failed to extract name :", e)