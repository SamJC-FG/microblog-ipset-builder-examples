import urllib.request

IPSET = []
IPLISTLINK = "https://my.pingdom.com/probes/ipv4"
IPLIST = urllib.request.urlopen(IPLISTLINK)
for ADDRESS in IPLIST:
    IPSETENTRY = (ADDRESS.decode().rstrip() + '/32')
    IPSET.append(IPSETENTRY)