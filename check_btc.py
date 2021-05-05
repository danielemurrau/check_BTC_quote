
import argparse
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import time
import sys


def main():
    parser = argparse.ArgumentParser(description='Get realtime BTC quote from Coinmarketapi')
    parser.add_argument('-s', '-seconds', type=int,
                        help='Number of seconds to refresh quota')
    parser.add_argument('-a', '-apikey', type=str,
                        help='Pass apikey from commandline')
   
    args = parser.parse_args()

    if len(sys.argv) < 2:
      print(''' usage: sys.argv[0] [-h] [-s] [-a]
      Get realtime BTC quote from Coinmarketapi
      optional arguments:
      -h , --help    show this help message and exit
      -s , -seconds  number of seconds to refresh quota
      -a , -apikey   Pass apikey from commandline''')
      exit(0)
    if args.s:
       s=args.s
       print ("Refresh every:", s)
    else:
       print("refresh tinme is neeeded")
       exit(0)

    if args.a:
       a=(args.a)
       print ("api key in use: " ,a)
    else:
       print("api key is neeeded")
       exit(0)

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
    'start':'1',
    'limit':'1',
    'convert':'EUR'
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': a, 
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
           print ("----------------------------------------------")
           time.sleep(s)
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)
        except KeyboardInterrupt:
            print("KeyboardInterrupt has been caught.")
            return
if __name__ == '__main__':
    main()