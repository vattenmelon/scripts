#!/usr/bin/python
import requests, sys, re

if len(sys.argv) < 2:
    print "Oppgi en valuta"
    sys.exit()
bitadr = sys.argv[1]
#print bitadr

def algo(x):
    return {
            0:'Scrypt',
            1:'SHA256',
            2:'ScryptNF',
            3:'X11',
            4:'X13',
            5:'Keccak',
            6:'X15',
            7:'Nist5',
            8:'NeoScrypt',
            9:'Lyra2RE',
            10:'WhirlpoolX',
            11:'Qubit',
            12:'Quark',
            13:'Axiom',
            14:'Lyra2REv2',
            15:'ScryptJaneNf16',
            16:'Blake256r8',
            17:'Blake256r14',
            18:'Blake256r8vnl',
            19:'Hodl',
            20:'DaggerHashimoto',
            21:'Decred',
            22:'CryptoNight',
            23:'Lbry',
            24:'Equihash',
            25:'Pascal',
            26:'X11Gost',
            27:'Sia',
            28:'Blake2s',
            29:'Skunk',
            }.get(x,'unknown')

url = "https://api.nicehash.com/api?method=stats.provider&addr="+bitadr
r = requests.get(url)
data = r.json()
#print data
if len(data) > 0:
    print 'Bitcoin adress: ' +  data['result']['addr']
    for x in data['result']['stats']:
        print '-----------------------------------'
        print 'algorithm:.......',algo(x['algo'])
        print 'accepted speed:..',x['accepted_speed']
        print 'balance:.........',x['balance']+' (BTC)'
