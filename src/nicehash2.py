#!/usr/bin/python
import requests, sys, re, crypto

args = ['dummyarg','bitcoin','USD' ,'m']
btckurs = crypto.main(args)

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
    print 'Exchange rate of ' + btckurs + ' USD/BTC retrieved from coinmarketcap'
    total_unpaid = 0
    for x in data['result']['current']:
        print '-----------------------------------'
        print 'algorithm:.......',x['name']
        print 'profitability:...',x['profitability'] + ' (BTC/daily)'
        if 'a' in x['data'][0]:
            print 'acceptet speed:..',x['data'][0]['a']+ ' ' + x['suffix']
        if 'rs' in x['data'][0]:
            print 'rejected speed:..',x['data'][0]['rs']+ ' ' + x['suffix']
        print 'balance:.........',x['data'][1] + ' (BTC)'
        print 'balance (USD)....',float(x['data'][1]) * float(btckurs)
        total_unpaid = total_unpaid + float(x['data'][1])
    print '-----------------------------------'
    print 'total unpaid balance BTC', total_unpaid
    print 'total unpaid balance USD', total_unpaid * float(btckurs)
            #print 'accepted speed:..',x['accepted_speed']
            #print 'balance:.........',x['balance']+' (BTC)'
