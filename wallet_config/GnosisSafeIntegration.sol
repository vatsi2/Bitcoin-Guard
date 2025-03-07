// contracts/GnosisSafeIntegration.sol

contract SafeDelegator {
    using GnosisSafe for GnosisSafe.Safe;
    
    function executeDelegateCall(
        address to, 
        bytes memory data, 
        uint256 nonce,
        bytes[] memory signatures
    ) external {
        GnosisSafe.Safe safe = GnosisSafe.Safe(msg.sender);
        require(safe.isOwner(tx.origin), "Not owner");
        
        safe.approveHash(keccak256(data));
        (bool success, ) = safe.execTransaction(
            to, 
            0, 
            data, 
            Enum.Operation.DelegateCall,
            0, 0, 0, address(0), 
            signatures
        );
        require(success, "Tx failed");
    }
}
