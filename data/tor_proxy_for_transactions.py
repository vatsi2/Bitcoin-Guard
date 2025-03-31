import stem.process

tor_process = stem.process.launch_tor_with_config(
    config = {'SocksPort': '9050'}
)
