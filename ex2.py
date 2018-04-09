#!/usr/bin/env python

import yaml
from pprint import pprint as pp
from snmp_helper import snmp_get_oid_v3, snmp_extract

with open("../store/inventory/devices.yml") as f:
  devices = yaml.load(f)

snmp_device = (devices['devices'][1]['ip_addr'],161)
snmp_user = (devices['devices'][1]['snmpv3_user'],
             devices['devices'][1]['snmpv3_auth'],
             devices['devices'][1]['snmpv3_auth'])
mib_row = 5
print(snmp_device)
print(snmp_user)
OID = '1.3.6.1.2.1.1.5.0' #hostname

snmp_data = snmp_get_oid_v3(snmp_device, snmp_user, oid=OID)
output = snmp_extract(snmp_data)
print(output)
  

