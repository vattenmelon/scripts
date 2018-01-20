#!/usr/bin/python
import requests, sys, re

if len(sys.argv) < 2:
    print "Oppgi en bitcoinadresse"
    sys.exit()
bitadr = sys.argv[1]

url = "https://api.nicehash.com/api?method=stats.provider.ex&addr="+bitadr
r = requests.get(url)
data = r.json()
#print data
if len(data) > 0:
    if 'error' in data['result']:
        print data['result']['error'] 
        sys.exit()
    print 'Bitcoin address: ' + data['result']['addr']
    for x in data['result']['current']:
        print '-----------------------------------'
        print 'algorithm:.......',x['name']
        print 'profitability:...',x['profitability'] + ' (BTC/daily)'
        if 'a' in x['data'][0]:
            print 'acceptet speed:..',x['data'][0]['a']+ ' ' + x['suffix']
        if 'rs' in x['data'][0]:
            print 'rejected speed:..',x['data'][0]['rs']+ ' ' + x['suffix']
        print 'balance:.........',x['data'][1] + ' (BTC)'
            #print 'accepted speed:..',x['accepted_speed']
            #print 'balance:.........',x['balance']+' (BTC)'
