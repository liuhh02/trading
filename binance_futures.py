import logging
import requests
import pprint

logger = logging.getLogger()

def get_contracts():
    res = requests.get("https://testnet.binancefuture.com/fapi/v1/exchangeInfo")
    pprint.pprint(res.status_code)

    contracts = []

    for contract in res.json()['symbols']:
        print(contract['pair'])
        contracts.append(contract['pair'])
    
    return contracts

print(get_contracts())