import CCXT from 'ccxt';  // CCXT unified API :contentReference[oaicite:12]{index=12}

async function marketOrder() {
  const binance = new CCXT.binance({ apiKey:'KEY', secret:'SECRET' });
  const order = await binance.createMarketBuyOrder('BTC/USDT', 0.005);
  console.log(order);
}

marketOrder();
