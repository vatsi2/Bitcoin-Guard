from cryptography.fernet import Fernet

def encrypt_vault(data, key):
    cipher = Fernet(key)
    return cipher.encrypt(data.encode())
