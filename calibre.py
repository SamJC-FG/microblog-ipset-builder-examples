import json
import urllib.request

IPSET = []
IPLISTLINK = "https://calibreapp.com/agents.json" #Fetch the Calibre agent IPs
RESPONSE = urllib.request.urlopen(IPLISTLINK)
DATA = json.loads(RESPONSE.read())
for ENTRY in DATA:
    IPADDR = ENTRY['ipv4'] #Fetch the ipv4 value in the dictionary
    IPSET.append(IPADDR + '/32') #Tack on a '/32' to the entry, and append it to the list

print(IPSET)