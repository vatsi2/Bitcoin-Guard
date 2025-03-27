import websockets  
import json  
from alerts import SMSAlert, EmailAlert  

class WhaleWatcher:  
    def __init__(self, threshold=50):  
        self.threshold = threshold  # BTC  
        self.alerts = [SMSAlert(), EmailAlert()]  

    async def monitor_bitcoin(self):  
        async with websockets.connect("wss://blockchain.info/ws") as ws:  
            await ws.send('{"op":"unconfirmed_sub"}')  
            while True:  
                tx = json.loads(await ws.recv())  
                if self._is_whale_tx(tx):  
                    self.trigger_alerts(tx)  

    def _is_whale_tx(self, tx):  
        return any(output['value'] > self.threshold * 1e8  
                   for output in tx['out'])  

    def trigger_alerts(self, tx):  
        message = f"Whale Alert: {tx['hash']} moved {self.threshold}+ BTC"  
        for alert in self.alerts:  
            alert.send(message)  
