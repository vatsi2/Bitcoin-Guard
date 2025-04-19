-- Strategy: Binance Order
-- Language: Haskell
-- Exchange: Binance (Spot)

import Binance.Client

main :: IO ()
main = do
  client <- newClient "KEY" "SECRET"
  resp <- placeOrder client LimitBuy "BTCUSDT" 0.01 (Just 29000)
  print resp
