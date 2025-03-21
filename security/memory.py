from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad

class RAMEncryptor:
    def __init__(self, key=None):
        self.key = key or secrets.token_bytes(32)
        self.iv = secrets.token_bytes(16)

    def encrypt(self, data):
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return cipher.encrypt(pad(data, AES.block_size))

    def decrypt(self, ciphertext):
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return unpad(cipher.decrypt(ciphertext), AES.block_size)
