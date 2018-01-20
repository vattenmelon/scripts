#!/usr/bin/python
import requests, sys, re
def main(args):
    if len(args) < 2:
        print "Oppgi en valuta"
        sys.exit()
    valuta = args[1].upper()
    if len(args) < 3:
        convert_to = ''
    else:
        convert_to = args[2].lower()

    url = "https://api.coinmarketcap.com/v1/ticker/"+valuta+"/?convert="+convert_to
    r = requests.get(url)
    data = r.json()
    #print data
    if len(data) > 0:
        if 'm' in args:
            return data[0]['price_'+convert_to]
        else: 
            if len(args) == 3:
                print convert_to.upper()+': ' + data[0]['price_'+convert_to]
            print 'USD: ' + data[0]['price_usd']
            print 'BTC: ' + data[0]['price_btc']
    else:
        print 'fant ikke valuta'

if __name__ == '__main__':
    main(sys.argv)
