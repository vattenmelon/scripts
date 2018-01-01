#!/usr/bin/python
import requests, sys, re

if len(sys.argv) < 2:
    print "Oppgi en valuta"
    sys.exit()
valuta = sys.argv[1].upper()
if len(sys.argv) < 3:
    convert_to = ''
else:
   convert_to = sys.argv[2].lower()

url = "https://api.coinmarketcap.com/v1/ticker/"+valuta+"/?convert="+convert_to
r = requests.get(url)
data = r.json()
#print data
if len(data) > 0:
    if len(sys.argv) == 3:
        print convert_to.upper()+': ' + data[0]['price_'+convert_to]
    print 'USD: ' + data[0]['price_usd']
    print 'BTC: ' + data[0]['price_btc']
else:
    print 'fant ikke valuta'
