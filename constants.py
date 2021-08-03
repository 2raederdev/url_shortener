import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

BITLY_API_KEY = os.getenv('BITLY_API_KEY')
