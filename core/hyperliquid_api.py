import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

class HyperliquidClient:
    def __init__(self, api_key: str):
        self.session = requests.Session()
        retries = Retry(
            total=3,
            backoff_factor=0.3,
            status_forcelist=[500, 502, 503, 504]
        )
        self.session.mount('https://', HTTPAdapter(max_retries=retries))
        
    def get_orderbook(self, symbol: str) -> dict:
        """Get L3 orderbook with institutional-grade retries"""
        return self._authenticated_request(
            "GET", f"/orderbook/{symbol}"
        )
