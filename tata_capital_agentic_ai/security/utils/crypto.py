from cryptography.fernet import Fernet
import base64
import os
from dotenv import load_dotenv

load_dotenv()

AES_SECRET_KEY = os.getenv("AES_SECRET_KEY")

if not AES_SECRET_KEY or len(AES_SECRET_KEY) != 32:
    raise ValueError("AES_SECRET_KEY must be exactly 32 characters")

FERNET_KEY = base64.urlsafe_b64encode(AES_SECRET_KEY.encode())
fernet = Fernet(FERNET_KEY)

def encrypt_data(data: str) -> str:
    """Encrypt sensitive data"""
    return fernet.encrypt(data.encode()).decode()

def decrypt_data(data: str) -> str:
    """Decrypt sensitive data"""
    return fernet.decrypt(data.encode()).decode()
