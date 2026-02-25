import os
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

    
    def ask_about_celebrity(self, name : str, question : str):
        try:

            headers = {
                "Authorization" : f"Bearer {self.api_key}",
                "Content-Type" : "application/json"
            }

            prompt = """
                        You are a AI Assistant that knows a lot about celebrities. You have to answer questions about {name} concisely and accurately.
                        Question : {question}
                     """
            
            payload = {
                "model" : self.model,
                "messages" : [
                        {
                            "role" : "user",
                            "content" : prompt
                        }
                ],
                "temperature" : 0.5,
                "max_tokens" : 512
            }

            response = requests.post(
                self.api_url,
                headers = headers,
                json = payload
                )
            
            if response.status_code == 200:
                return response.json()['choices'][0]['message']['content']
            
            return "Sorry I coudn't find the answer"
        
        except Exception as e:
            logger.error(f"Error while generating answers related to user questions : {e}")
            raise CustomException("Failed to nswers related to user questions : ", e)