import requests

def is_sanctioned(address):
    ofac_list = requests.get('https://api.treasury.gov/sdn')
    return address in ofac_list.json()
