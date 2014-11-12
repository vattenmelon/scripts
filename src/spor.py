#!/usr/local/bin/python
import requests, sys, re

POSTEN_URL = "http://sporing.bring.no/sporing.json?q="

if len(sys.argv) != 2:
    print "Oppgi ett sporingsnummer!"
    sys.exit(1)
    
try:
    r = requests.get("{0}{1}".format(POSTEN_URL, sys.argv[1]))
except requests.exceptions.ConnectionError as e:
    print "Nettverksfeil: {0}".format(e)
    sys.exit(1)

#print data
data = r.json()

if 'error' in data['consignmentSet'][0]:
    print 'Fant ikke sporingsummer'
    sys.exit()

print "======== " + sys.argv[1] + " ======== " + data['consignmentSet'][0]['packageSet'][0]['productName'] + " / " + data['consignmentSet'][0]['packageSet'][0]['brand'] + " ======="
for z in data['consignmentSet'][0]['packageSet'][0]['eventSet']:
    print z['displayDate'] + ' ' + z['displayTime'] + ' ' + re.sub('<[^<]+?>', '', z['description']) + " (" + z['city'] + ' ' + z['country'] + ")"
