from bip32 import BIP32
from cryptography.hazmat.primitives import hashes

def generate_mnemonic(strength=256):
    # Let's use CSPRNG (Cryptographically Secure PRNG)
    entropy = os.urandom(strength // 8)
    h = hashes.Hash(hashes.SHA256())
    h.update(entropy)
    checksum = h.finalize()[:strength // 32]
    return BIP39.encode(entropy + checksum)
