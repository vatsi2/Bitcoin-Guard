from cryptography.hazmat.primitives.asymmetric import ed25519

def verify_update(signature, data, pub_key):
    public_key = ed25519.Ed25519PublicKey.from_public_bytes(pub_key)
    try:
        public_key.verify(signature, data)
        return True
    except:
        return False
