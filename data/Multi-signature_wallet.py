from bitcoinlib.wallets import Wallet

wallet = Wallet.create('Royen', keys=[
    'LedgerXPub1', 
    'TrezorXPub2', 
    'ColdcardXPub3',
    'MetaMaskPub4',
    'BitBox02Pub5'
], sigs_required=3)
