from quixstreams import Application
from constants import COINMARKET_API
from requests import Session
import json
from pprint import pprint

def get_latest_coin_data(target_symbol = "BTC"):
    API_URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"

    parameters = {
    'symbol': target_symbol,
    'convert':'USD'
    }

    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': COINMARKET_API,
    }

    session = Session()
    session.headers.update(headers)


    response = session.get(API_URL, params=parameters)
    return json.loads(response.text)

if __name__ == '__main__':
    coin_data = get_latest_coin_data()

    pprint(coin_data)