#!/usr/local/bin/python
import requests, sys, re

CLIENT_ID='postnr.py'
COUNTRY='no'

if len(sys.argv) != 2:
    print "Oppgi et postnummer"
    sys.exit()

posten_url = "https://api.bring.com/shippingguide/api/postalCode.json?clientUrl="+CLIENT_ID+"&country="+COUNTRY+"&pnr="+sys.argv[1]
r = requests.get(posten_url)
data = r.json()
#print data

print data['result']
