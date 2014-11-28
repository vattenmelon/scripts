#!/usr/bin/python
import requests, sys, re
reload(sys)
sys.setdefaultencoding('utf-8')
param = '' 
if (len(sys.argv) > 1 ):
    param = sys.argv[1]

side = 1
flere = True 
while flere:
    url = 'http://hotell.difi.no/api/json/ssb/regioner/landkoder?query='+param+'&page='+str(side)
    r = requests.get(url)
    data = r.json()
    if int(data['pages']) == 0:
            sys.exit(0)
    if int(data['page']) == int(data['pages']):
        flere = False
    side = side + 1
    for z in data['entries']:
        print z['kode'] + ' - ' + z['tittel'] + ' - ' + z['k_tittel']
