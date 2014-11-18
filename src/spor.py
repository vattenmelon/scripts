#!/usr/local/bin/python
import requests, sys, re

POSTEN_URL = "http://sporing.bring.no/sporing.json?q="

if len(sys.argv) < 2:
    print "Oppgi ett sporingsnummer!"
    sys.exit(1)

description = ""
if len(sys.argv) == 3:
    description = " - " + sys.argv[2]
   
try:
    r = requests.get("{0}{1}".format(POSTEN_URL, sys.argv[1]))
except requests.exceptions.ConnectionError as e:
    print "Nettverksfeil: {0}".format(e)
    sys.exit(1)

data = r.json()
#print data

if 'error' in data['consignmentSet'][0]:
    print sys.argv[1] +  ' Fant ikke sporingsummer' + description
    sys.exit()

print "======== " + sys.argv[1] + " ======== " + data['consignmentSet'][0]['packageSet'][0]['productName'] + " / " + data['consignmentSet'][0]['packageSet'][0]['brand'] + " =======" + description 
teller = len(data['consignmentSet'][0]['packageSet'][0]['eventSet']) 
for z in data['consignmentSet'][0]['packageSet'][0]['eventSet']:
    print "   " + str(teller) + " -  " +  z['displayDate'] + ' ' + z['displayTime'] + ' ' + re.sub('<[^<]+?>', '', z['description']) + " (" + z['city'] + ' ' + z['country'] + ")"
    teller = teller - 1
