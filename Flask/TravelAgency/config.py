from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_URI = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@localhost:5432/travel_agency'