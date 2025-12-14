VPNwatcher for OS X
###################
:date: 2015-06-30 21:55
:author: admin
:category: Uncategorized
:slug: vpnwatcher-for-os-x
:status: published
:save_as: 2015/06/30/vpnwatcher-for-os-x/index.html
:url: 2015/06/30/vpnwatcher-for-os-x/

Swap out "Transmission" for your own VPN-sensitive client, obvs. Assumes Viscosity or another client that creates a tun0 interface.

:literal:`while [ 1 ]; do if [ -z "\`ifconfig | grep tun0\`" ]; then ps ax | grep -i Transmission | grep -v grep | awk '{print $1}' | xargs kill; echo "killed process at \`date\`"; exit 1; fi; sleep 1; done`
