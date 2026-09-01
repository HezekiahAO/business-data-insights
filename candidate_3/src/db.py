# src/db.py
"""
db.py
Single responsibility: manage the Postgres connection.
No business logic here — just open/close cleanly, credentials from .env.
"""
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    """Open a new Postgres connection using credentials from .env."""
    return psycopg2.connect(
        host="localhost",
        dbname="postgres",
        user="postgres",
        password=os.getenv("DB_PASSWORD"),
    )