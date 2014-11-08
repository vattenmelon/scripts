#!/usr/local/bin/python
import requests, sys

if len(sys.argv) == 1:
    print "oppgi sporingsnummer!"
    sys.exit()
    

github_url = "http://sporing.bring.no/sporing.json?q="+sys.argv[1]
r = requests.get(github_url)
data = r.json()
print "sporingsnummer " + sys.argv[1]
for z in data['consignmentSet'][0]['packageSet'][0]['eventSet']:
    print z['displayDate'] + ' ' + z['displayTime'] + ' ' + z['description'] + " (" + z['city'] + ' ' + z['country'] + ")"