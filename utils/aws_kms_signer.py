from aws_kms_signer import KMSSigner

class AwsSecureSigner:
    def __init__(self, key_id: str):
        self.signer = KMSSigner(key_id)
        
    def sign_transaction(self, tx: dict) -> bytes:
        return self.signer.sign(tx)
