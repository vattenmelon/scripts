#!/usr/local/bin/python
import requests, sys, re

if len(sys.argv) != 2:
    print "Oppgi en kommune!"
    sys.exit()

url = "http://hotell.difi.no/api/json/ssb/regioner/kommuner?query="+sys.argv[1]
r = requests.get(url)
data = r.json()
#print data

for z in data['entries']:
    print z['kode']
