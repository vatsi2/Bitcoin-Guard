def whirlpool_mix(utxos, pool_id='0.01btc'):
    coordinator = WhirlpoolCoordinator()
    return coordinator.mix(
        utxos,
        pool_id=pool_id,
        anon_score_target=5
    )
