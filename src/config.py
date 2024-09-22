import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BUCKET_KEY_ID = os.getenv('BUCKET_KEY_ID')
    BUCKET_KEY = os.getenv('BUCKET_KEY')
    REGION = os.getenv('REGION')
    DATABASE_NAME = os.getenv('DATABASE_NAME')
    DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
    DB_URL = os.getenv('DB_URL')

    
config = Config()
