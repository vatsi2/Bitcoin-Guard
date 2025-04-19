// Strategy: Binance Order
// Language: Dart
// Exchange: Binance (Spot)
import 'package:binance/binance.dart';

void main() async {
  final client = Binance(apiKey: 'KEY', secret: 'SECRET');
  final order = await client.createOrder('BTCUSDT', 'BUY', 'LIMIT', '0.01', price:'29000');
  print(order);
}
