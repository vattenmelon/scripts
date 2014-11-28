#!/usr/bin/python
import requests, sys, json, locale
from datetime import datetime

URL = "https://www.norsk-tipping.no/api-lotto/getResultInfo.json"

r = requests.get(URL)
data = r.text
data = data.replace("while(true);/* 0;", "")
data = data.replace("/* */","")
data = data.strip()
json = json.loads(data)
date = datetime.strptime(json['drawDate'], '%Y,%m,%d,%H,%M,%S')
print 'Dato         ' + date.strftime('%d. %b %Y - %H.%M.%S') 
print 'Rekke        ' + ", ".join("{0}".format(n) for n in (json['mainTable']))
print 'Tilleggstall ' + ", ".join("{0}".format(n) for n in (json['addTable']))
for i in range (0, len(json['prizeTable'])):
    print '{:12s}: {:10,} kr'.format(json['prizeCaptionTable'][i], int(json['prizeTable'][i])).replace(',', ' ') 
