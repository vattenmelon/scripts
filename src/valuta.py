#!/usr/bin/python
import requests, sys, re

if len(sys.argv) != 2:
    print "Oppgi en valuta"
    sys.exit()
valuta = sys.argv[1].upper()
url = "http://www.freecurrencyconverterapi.com/api/v2/convert?q="+valuta+"_NOK&compact=y"
r = requests.get(url)
data = r.json()
#print data

print data[valuta+'_NOK']['val']
