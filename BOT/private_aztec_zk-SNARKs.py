def create_private_derivative(position: DerivatvePosition, aztec_sdk: Aztec) -> ZKProof:
    private_params = aztec_sdk.encrypt(position.details)
    proof = zk_prover.generate(
        circuit="derivative_valid",
        inputs={**private_params, "public": position.public_data}
    )
    return proof.submit_to_l2(ARBITRUM_RPC)
