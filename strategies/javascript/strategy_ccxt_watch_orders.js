const ccxtpro = require('ccxt.pro');  // CCXT Pro websockets :contentReference[oaicite:9]{index=9}

;(async () => {
  const exchange = new ccxtpro.binance({ apiKey:'KEY', secret:'SECRET' });
  while (true) {
    const orders = await exchange.watchOrders();  // real-time order updates
    console.log(orders);
  }
})();
