// components/WalletSelector.jsx

import { useConnect, MetaMask, TrustWallet, Ledger } from '@web3-react/core'

export default function WalletSelector() {
  const { connect } = useConnect()
  
  return (
    <div className="wallet-grid">
      <Button onClick={() => connect(MetaMask())}>
        <MetaMaskIcon /> Connect MetaMask
      </Button>
      
      <Button onClick={() => connect(TrustWallet())}>
        <TrustWalletIcon /> Trust Wallet
      </Button>
      
      <Button onClick={() => connect(Ledger())}>
        <LedgerIcon /> Ledger
      </Button>
      
      <FireblocksConnect 
        apiKey={import.meta.env.VITE_FIREBLOCKS_KEY}
        vaultIds={[1, 3]}
      />
    </div>
  )
}
