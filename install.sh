#!/usr/bin/env bash

set -o errexit
set -o pipefail

# Check if user is root
if [[ $(id -u) -ne 0 ]] ; then echo "Please run as super user." ; exit 1 ; fi

# Install python
apt-get update
apt-get install -y python3 python3-pip python3-venv virtualenv curl wget
# Install iptables-persistent to persist rules
echo iptables-persistent iptables-persistent/autosave_v4 boolean true | sudo debconf-set-selections
echo iptables-persistent iptables-persistent/autosave_v6 boolean true | sudo debconf-set-selections
apt-get install -y iptables-persistent
chmod 777 /etc/iptables/rules.v4
chmod 777 /etc/iptables/rules.v6

# Setup virtual environment
virtualenv -p python3 venv
source venv/bin/activate

# Install requirements
pip3 install -r requirements.txt
deactivate

# remove ufw
apt-get purge ufw -y

# Flush iptables at the first
iptables -F

# Install ipset
apt-get install ipset -y


chmod +x run.sh

echo "Making grpc credentials"
IP=`curl ifconfig.me`
mkdir -p /root/.smartEyes/grpc/
cd /root/.smartEyes/grpc/
echo "Generating certs for ip: ${IP}"
sed -i "/\[ v3_ca \]/a\subjectAltName = IP:${IP}" /etc/ssl/openssl.cnf
openssl req -newkey rsa:2048 -new -nodes -x509 -days 3650 -keyout key.key -out cert.crt -subj "/C=NL/ST=example/L=example/O=example/OU=IT Department/CN=${IP}"


echo "Installed successfully."
