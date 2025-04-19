package main

import "github.com/fiatjaf/go-bitcoin-rpc"

func main() {
    client := rpc.New("http://user:pass@127.0.0.1:8332")
    // TODO: monitor RBTC pools, distribute yield
    _ = client
}
