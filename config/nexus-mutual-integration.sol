// contracts/insurance/NexusIntegration.sol

contract NexusAdapter is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;
    
    INexusCover public immutable nexusCover;
    
    constructor(address _nexus) {
        nexusCover = INexusCover(_nexus);
    }

    /// Покупка страховки при достижении TVL
    function purchaseCover(uint256 vaultId, uint256 amount) external {
        Vault storage vault = vaults[vaultId];
        require(vault.tvl >= 1_000_000 ether, "Min TVL $1M");
        
        uint256 premium = nexusCover.calculatePremium(
            address(this), 
            amount, 
            30 days
        );
        
        IERC20(USDC).safeTransferFrom(msg.sender, address(this), premium);
        nexusCover.buyCover{value: premium}(
            vaultId, 
            amount, 
            30 days
        );
        
        emit InsurancePurchased(vaultId, amount);
    }
}
