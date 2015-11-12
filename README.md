# prepend a nameserver to NetworkManager connections

A dispatcher script for NetworkManager on Debian to ensure that when the dhcp state of an interface changes, we push some nameservers in front of whatever the connection thinks the nameserver list ought to be.

the idea is to make a local-only nameserver, (such as dnsmasq) be consulted ahead of any other nameservers, so I can resolve fake domains for vms, containers etc.

the script writes out the original nameserver list in a resolv.conf style to a file, which can then be used as a forwarder by the local-only nameserver to preserve original DNS lookup behaviour

It's intended to be run out of /etc/NetworkManager/dispatcher.d/ , which means it will be called with the expected arguments and environment
