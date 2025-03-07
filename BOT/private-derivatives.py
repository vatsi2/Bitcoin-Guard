proof = aztec.create_proof(
    action="buy_derivative",
    params={"amount": "1M", "expiry": "2024-12-31"},
    public_data={"user": "0x..."}
)
