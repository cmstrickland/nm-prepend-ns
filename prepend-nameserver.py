#!/usr/bin/env python3
import sys
import os


prepend_nameservers = [ '172.20.0.1' ]
dnsmasq_resolv_conf = '/var/lib/lxc/upstream-resolv.conf'

connection = os.getenv('CONNECTION_UUID')

# Network manager passes an interface name and an event type in as args
[iface, evt] = sys.argv[1:]

#nm provides the resolver nameservers list in an env variable
def get_ns_list(spaced_str=None):
    if spaced_str == None:
        spaced_str = os.getenv('IP4_NAMESERVERS')
    return spaced_str.split(' ')


if evt == 'dhcp4-change' and iface == 'wlan0' :
    nameservers = get_ns_list()
    if nameservers[0] != prepend_nameservers[0]:
        new_nameservers = prepend_nameservers + nameservers
        subprocess.call(["nmcli", "con", "mod", connection,
                         "ipv4.dns", ','.join(new_nameservers)])
        with open(dnsmasq_resolv_conf,'w') as upstream:
            upstream.writelines( "{}\n".format(server) for server in nameservers )
