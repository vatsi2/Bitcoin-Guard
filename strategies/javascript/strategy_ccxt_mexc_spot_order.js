const ccxt = require('ccxt');
(async () => {
  const mexc = new ccxt.mexc3({ apiKey:'KEY', secret:'SECRET', options:{ defaultType:'spot' } });
  const balance = (await mexc.fetchBalance()).free.USDT;
  const price = (await mexc.fetchTicker('ETH/USDT')).last;
  const amount = balance / price;
  await mexc.createOrder('ETH/USDT','immediate_or_cancel','buy',amount);  // MEXC IOC order :contentReference[oaicite:10]{index=10}
})();
