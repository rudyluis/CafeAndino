from __future__ import annotations
import os
from pathlib import Path
from dotenv import load_dotenv
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / '.env')

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-change-me')
    DEMO_USER = os.getenv('DEMO_USER', 'admin')
    DEMO_PASSWORD = os.getenv('DEMO_PASSWORD', '123456')
    DEMO_FULL_NAME = os.getenv('DEMO_FULL_NAME', 'Administrador Demo')
    WTF_CSRF_TIME_LIMIT = None
