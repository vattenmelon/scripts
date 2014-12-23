#!/usr/bin/python
import requests, sys, re

if len(sys.argv) != 2:
    print "Oppgi en valuta"
    sys.exit()

url = "http://www.freecurrencyconverterapi.com/api/v2/convert?q="+sys.argv[1]+"_NOK&compact=y"
r = requests.get(url)
data = r.json()
#print data

print data[sys.argv[1]+'_NOK']['val']
