import logging
import requests
import pprint

logger = logging.getLogger()

def get_contracts():
    res = requests.get("https://ftx.com/api/markets")
    pprint.pprint(res.status_code)
    # print(res.json())

    contracts = []

    for contract in res.json()['result']:
        #print(contract['name'])
        contracts.append(contract['name'])
    
    return contracts

print(get_contracts())