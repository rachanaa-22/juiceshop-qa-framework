import os
from dotenv import load_dotenv

load_dotenv()

USER_EMAIL = os.getenv("USER_EMAIL", "admin@juice-sh.op")
USER_PASSWORD = os.getenv("USER_PASSWORD", "admin123")