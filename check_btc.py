#__author__ = "Daniele Murrau"
#__version__ = "0.1.0"
#__status__ = "Dev"

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import time

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
          'start':'1',
            'limit':'1',
              'convert':'EUR'
              }
headers = {
          'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': 'INSERT HERE YOUR COINMARKETCAP API KEY',
            }

session = Session()
session.headers.update(headers)
while True:
    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        print ("----------------------------------------------")
        print (data['status']['timestamp'] + " ", end = '')
        print (data['data'][0]['name'] + " ", end = '')
        print (data['data'][0]['symbol'] + " ", end = '')
        print (data['data'][0]['quote']['EUR']['price'])
        time.sleep(5)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
