import shutil
import os

def emergency_wipe():
    shutil.rmtree('/vaults')
    os.remove('bitguard.db')
    overwrite_free_space() # Gutmann method
