const ccxt = require('ccxt');  // CCXT unified API :contentReference[oaicite:8]{index=8}

(async () => {
  const exchange = new ccxt.binance({ apiKey:'KEY', secret:'SECRET' });
  const order = await exchange.createOrder('BTC/USDT','limit','buy',0.01,29500);
  console.log(order);
})();
