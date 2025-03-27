def social_recovery(shares):
    # 3-of-5 Shamir recuperation
    return SecretSharer.recover_secret(shares[:3])
