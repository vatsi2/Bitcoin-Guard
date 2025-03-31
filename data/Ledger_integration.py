from ledgerblue.comm import getDongle

dongle = getDongle(True)
apdu = construct_apdu("GET_WALLET_INFO")
response = dongle.exchange(apdu)
