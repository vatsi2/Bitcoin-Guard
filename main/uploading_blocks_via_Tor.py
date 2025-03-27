import stem.process
from stem.util import term

def start_tor_session():
    tor_process = stem.process.launch_tor_with_config(
        config = {
            'SocksPort': '9050',
            'ControlPort': '9051',
            'DataDirectory': '/tmp/tor-data'
        },
        init_msg_handler = lambda line: print(term.format(line, term.Color.BLUE))
    return tor_process
