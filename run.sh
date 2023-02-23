#! /bin/bash

if [[ $(id -u) -ne 0 ]]; then
  echo "Please run as super user."
  exit 1
fi

function usage {
  echo "Usage: run.sh --port [--help]"
  echo "   "
  echo "  --port         : port to bind the service with. E.g. 5050"
}

function parse_args {
  # Named args.
  while [[ "${1:-}" != "" ]]; do
    case "$1" in
    --port)
      PORT="$2"
      shift
      ;;
    --help)
      usage
      exit
      ;; # Quit and show usage
    esac
    shift
  done
}

parse_args "$@"

# Validate required args.
if [[ -z "${PORT:-}" ]]; then
  echo "Invalid arguments."
  usage
  exit
fi

iptables -C INPUT -p tcp --dport "$PORT" -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT &>/dev/null
if [[ $? -ne 0 ]]; then
  iptables -I INPUT 1 -p tcp --dport "$PORT" -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
fi

iptables -C OUTPUT -p tcp --sport $PORT -m conntrack --ctstate ESTABLISHED -j ACCEPT &>/dev/null
if [[ $? -ne 0 ]]; then
  iptables -A OUTPUT -p tcp --sport $PORT -m conntrack --ctstate ESTABLISHED -j ACCEPT
fi

iptables -C INPUT -i lo -j ACCEPT &>/dev/null
if [[ $? -ne 0 ]]; then
  iptables -I INPUT 2 -i lo -j ACCEPT
fi

iptables -C INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT &>/dev/null
if [[ $? -ne 0 ]]; then
  iptables -I INPUT 3 -m state --state ESTABLISHED,RELATED -j ACCEPT
fi

iptables -C INPUT -p tcp --dport 22 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT &>/dev/null
if [[ $? -ne 0 ]]; then
  iptables -A INPUT -p tcp --dport 22 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
fi

iptables -C OUTPUT -p tcp --sport 22 -m conntrack --ctstate ESTABLISHED -j ACCEPT &>/dev/null
if [[ $? -ne 0 ]]; then
  iptables -A OUTPUT -p tcp --sport 22 -m conntrack --ctstate ESTABLISHED -j ACCEPT
fi

netfilter-persistent save >/dev/null 2>&1
echo -n $PORT >PortNum

source ./venv/bin/activate
python3 main.py --port $PORT &

deactivate
