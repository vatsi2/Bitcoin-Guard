from config import Settings
from risk_management import RiskEngine
from hyperliquid_api import HyperliquidClient
from aave_integration import AaveManager
import logging

def main():
    """Orchestrate bot workflow with fail-safes"""
    try:
        config = Settings.load()
        RiskEngine.validate_config(config)
        
        hl_client = HyperliquidClient(config.hyperliquid_api)
        aave_manager = AaveManager(config.aave_rpc)
        
        while True:
            RiskEngine.check_system_health()
            execute_strategies(config, hl_client, aave_manager)
            
    except Exception as e:
        logging.critical(f"Fatal error: {e}", exc_info=True)
        RiskEngine.emergency_shutdown()

if __name__ == "__main__":
    main()
