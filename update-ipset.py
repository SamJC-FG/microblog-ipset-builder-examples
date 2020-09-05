import boto3

BOTOCLIENT_WAF = boto3.client('wafv2')

IPSETARN = '<THROW IN THE ARN of your target IPSet>' #In my project, I did some trickery invovling quering the stack WAF that's supplied via AWS EventBridge
AVAILABLEIPSETS = BOTOCLIENT_WAF.list_ip_sets(Scope=SCOPE)['IPSets']

for ipset in AVAILABLEIPSETS:
    if ipset['ARN'] == IPSETARN:
        IPSETID = ipset["Id"] #The IPSet Id, duh
        IPSETNAME = ipset["Name"] #The IPSet name

CALIBREIPSET = BOTOCLIENT_WAF.get_ip_set(
Name = IPSETNAME,
Scope = SCOPE,
Id = IPSETID

#No need to clear then update, it appears update_ip_set method does this. So you need to have your IPSet ready before updating
BOTOCLIENT_WAF.update_ip_set(
    Name = IPSETNAME,
    Scope = SCOPE,
    Id = IPSETID,
    Description = 'IPSet featuring addresses associated with Calibre. Updated dynamically via Calibre-ipset-builder Lambda.',
    Addresses = IPSET,
    LockToken = CALIBREIPSET.get('LockToken')