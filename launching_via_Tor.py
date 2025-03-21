import stem.process
from stem.util import term

def start_tor():
    print(term.format("Starting Tor...", term.Color.BLUE))
    tor_process = stem.process.launch_tor_with_config(
        config={
            "SocksPort": "9050",
            "ControlPort": "9051",
            "ExitNodes": "{fr}",
        },
        init_msg_handler=lambda line: print(line),
    )
    return tor_process

if __name__ == "__main__":
    tor_process = start_tor()
    config = load_config("config.yaml")
    mixer = CrossChainAnonymizer(config)
    mixer.run_mixing()
    tor_process.kill()
