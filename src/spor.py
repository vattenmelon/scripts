#!/usr/local/bin/python
import requests, sys, re

if len(sys.argv) != 2:
    print "Oppgi ett sporingsnummer!"
    sys.exit()
    

github_url = "http://sporing.bring.no/sporing.json?q="+sys.argv[1]
r = requests.get(github_url)
data = r.json()
#print data

if 'error' in data['consignmentSet'][0]:
    print 'Fant ikke pakke'
    sys.exit()

print "======== " + sys.argv[1] + " ========"
for z in data['consignmentSet'][0]['packageSet'][0]['eventSet']:
    print z['displayDate'] + ' ' + z['displayTime'] + ' ' + re.sub('<[^<]+?>', '', z['description']) + " (" + z['city'] + ' ' + z['country'] + ")"
