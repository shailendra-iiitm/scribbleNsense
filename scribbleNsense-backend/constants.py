# constants.py
from dotenv import load_dotenv
import os

load_dotenv()

SERVER_URL = 'localhost'
PORT = int(os.getenv('PORT', 8900))  # Use environment variable or fallback to 8900
ENV = os.getenv('ENV', 'dev')  # Use environment variable or fallback to 'dev'
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
