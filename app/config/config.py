import os
from dotenv import load_dotenv

load_dotenv()
class Config:

    api_key = os.getenv("GROQ_API_KEY")
    api_url = os.getenv("END_POINT_URL") or "https://api.groq.com/openai/v1/chat/completions"
    image_model = "meta-llama/llama-4-scout-17b-16e-instruct"
    chat_model = "meta-llama/llama-4-scout-17b-16e-instruct"