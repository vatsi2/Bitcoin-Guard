// tests/wallet_signing.rs

#[tokio::test]
async fn test_multisig_with_fireblocks() {
    let tx = Transaction::new(...);
    let signer = WalletProvider::Fireblocks(test_api_key());
    let sig = signer.sign_transaction(tx).await.unwrap();
    
    assert!(sig.verify(tx.sender));
}

#[tokio::test]
async fn test_metamask_signing() {
    let mock_rpc = MockJsonRpc::new().with_signer(Alice);
    let signer = WalletProvider::MetaMask(mock_rpc.url());
    let sig = signer.sign_transaction(tx).await.unwrap();
    
    assert_eq!(sig, expected_alice_sig);
}
