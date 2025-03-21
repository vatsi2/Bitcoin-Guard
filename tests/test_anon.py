import unittest
from unittest.mock import patch
from core import CrossChainAnonymizer

class TestAnonymizer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = {
            "networks": ["bitcoin_testnet"],
            "dao": "dummy",
            "security": {"delay": 0}
        }

    @patch('web3.eth.Eth.sendRawTransaction')
    def test_eth_deposit(self, mock_send):
        mixer = CrossChainAnonymizer(self.config)
        mixer.deposit_to_dao(0.1, "ETH")
        self.assertTrue(mock_send.called)

    def test_hd_wallet_generation(self):
        mixer = CrossChainAnonymizer(self.config)
        wallet = mixer._generate_hd_wallet("monero")
        self.assertEqual(len(wallet["seed"]), 64)

if __name__ == "__main__":
    unittest.main()
