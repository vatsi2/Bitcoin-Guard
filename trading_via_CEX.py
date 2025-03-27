# Binance trading module
import hmac
import hashlib
import requests

class BinanceTrader:
    def __init__(self, api_key, api_secret):
        self.base_url = "https://api.binance.com"
        self.api_key = api_key
        self.api_secret = api_secret
        
    def _sign_request(self, params):
        query = '&'.join([f"{k}={v}" for k,v in params.items()])
        return hmac.new(
            self.api_secret.encode(),
            query.encode(),
            hashlib.sha256
        ).hexdigest()
        
    def place_order(self, symbol, side, quantity):
        """Limit order placement"""
        params = {
            'symbol': symbol,
            'side': side.upper(),
            'type': 'LIMIT',
            'quantity': quantity,
            'timestamp': int(time.time() * 1000)
        }
        
        params['signature'] = self._sign_request(params)
        
        headers = {'X-MBX-APIKEY': self.api_key}
        response = requests.post(
            f"{self.base_url}/api/v3/order",
            params=params,
            headers=headers
        )
        return response.json()

# Utilization
trader = BinanceTrader('API_KEY', 'API_SECRET')
order = trader.place_order('BTCUSDT', 'BUY', 0.1)
print(f"Ордер размещен: {order['orderId']}")
