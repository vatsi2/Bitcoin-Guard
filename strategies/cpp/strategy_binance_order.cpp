#include "binance_api.h"  // Hypothetical C++ SDK

int main() {
    Binance::Client client("KEY","SECRET");
    auto order = client.createOrder("BTCUSDT","BUY","LIMIT",0.01,29000);
    std::cout << order.toJson() << std::endl;
}
