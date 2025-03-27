import requests  
from threading import Timer  

class DarkWebScanner:  
    API_ENDPOINT = "https://threatintel.example.com/v1/check"  

    def __init__(self, addresses, api_key):  
        self.addresses = addresses  
        self.api_key = api_key  

    def scan_address(self, address):  
        resp = requests.post(  
            self.API_ENDPOINT,  
            json={"address": address},  
            headers={"X-API-Key": self.api_key}  
        )  
        return resp.json().get('found', False)  

    def continuous_scan(self):  
        for addr in self.addresses:  
            if self.scan_address(addr):  
                self._handle_leak(addr)  
        Timer(3600 * 6, self.continuous_scan).start()  

    def _handle_leak(self, address):  
        print(f"EMERGENCY: {address} leaked! Rotating keys...")  
        # Implement key rotation logic  
