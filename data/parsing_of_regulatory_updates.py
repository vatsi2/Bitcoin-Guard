import ipfshttpclient

client = ipfshttpclient.connect()
regulatory_updates = client.cat('QmRegulatoryHash')
