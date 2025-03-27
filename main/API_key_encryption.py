from cryptography.fernet import Fernet

def encrypt_api_key(key, password):
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), iterations=100000)
    salt = os.urandom(16)
    key = base64.urlsafe_b64encode(kdf.derive(password))
    cipher = Fernet(key)
    return cipher.encrypt(key), salt
