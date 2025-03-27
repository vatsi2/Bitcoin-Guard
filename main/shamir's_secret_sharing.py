from secretsharing import SecretSharer

def split_seed(seed, shares=5, threshold=3):
    return SecretSharer.split_secret(seed, threshold, shares)
