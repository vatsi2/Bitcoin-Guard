# wallets/eth_connector.py

class EVMWalletManager:
    def __init__(self, provider: str):
        if provider == "metamask":
            self.wallet = MetaMaskConnector("http://localhost:8545")
        elif provider == "trust":
            self.wallet = TrustWalletConnector(chain_id=1)
        elif provider == "fireblocks":
            self.wallet = FireblocksSDK(os.getenv("FIREBLOCKS_KEY"))

    def sign_tx(self, tx: dict) -> HexBytes:
        if isinstance(self.wallet, MetaMaskConnector):
            return self.wallet.personal_sign(tx)
        else:
            return self.wallet.sign_transaction(tx)
