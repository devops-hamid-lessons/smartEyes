#! /bin/bash

if [[ $(id -u) -ne 0 ]] ; then echo "Please run as super user." ; exit 1 ; fi

function exit_if_failed() {
  if [[ "$1" -ne 0 ]]; then
    echo "$2"
    iptables -P INPUT ACCEPT
    exit 1
  fi
}

iptables -F
exit_if_failed $? 'Error: unable to do flush. Try again.'
iptables -A INPUT -p tcp --dport $(cat PortNum) -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
exit_if_failed $? 'Error: unable to open service port. Try again.'
iptables -A INPUT -i lo -j ACCEPT
exit_if_failed $? 'Error: unable to open loop-back interface. Try again.'
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
exit_if_failed $? 'Error: unable to add rule for connections started from the host itself. Try again.'
iptables -A INPUT -p tcp --dport 22 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
exit_if_failed $? 'Error: unable to open ssh. Try again.'
netfilter-persistent save
exit_if_failed $? 'Error: unable to save rules. Try again.'
exit 0
