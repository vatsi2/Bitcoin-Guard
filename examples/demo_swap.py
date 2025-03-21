from core import CrossChainAnonymizer
import yaml

def main():
    with open("config_demo.yaml") as f:
        config = yaml.safe_load(f)
    
    mixer = CrossChainAnonymizer(config)
    print("Starting ETH → XMR swap via THORChain...")
    mixer.cross_chain_swap("ETH", "XMR", 0.5)
    print("Swap completed. Check your Monero wallet.")

if __name__ == "__main__":
    main()
