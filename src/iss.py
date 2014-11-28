#!/usr/bin/python
import requests, sys, re

CARDNUMBER = '' 
PIN = '' 

URL = "http://icare.myissworld.net/loginAction.do"
QUERYPARAMS = "?requiresPIN=true&redirectUrl=&iCardNumber={0}&styleDir=&PIN={1}&language="

if CARDNUMBER == '' or PIN == '':
    print 'Sett kortnummer og pin i scriptet'
    sys.exit(1)

FORMATTED_URL = URL + QUERYPARAMS.format(CARDNUMBER, PIN)

#print FORMATTED_URL

r = requests.get(FORMATTED_URL)
htmltext = r.text
#print htmltext
m = re.search('<!--([\d]*[.][\d]*) -->', htmltext)
numberAsString = m.group(1)
print 'Kr {0:.2f}'.format(float(numberAsString))
