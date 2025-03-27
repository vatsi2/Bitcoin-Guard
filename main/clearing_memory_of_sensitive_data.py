import ctypes

def secure_erase(buffer):
    memset = ctypes.cdll.msvcrt.memset
    memset(buffer, 0, len(buffer))
    del buffer
