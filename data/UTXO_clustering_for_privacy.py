def cluster_utxos(utxos, threshold=0.01):
    return DBSCAN(eps=threshold).fit_predict(utxos)
