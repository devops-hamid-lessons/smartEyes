import os
import subprocess
from libs.utils import command_parser, CHAINS


class IPTable:

    @staticmethod
    def ListRules(chain):
        rules = os.popen(
            'iptables -S {chain}'.format(chain=CHAINS[chain])).read()
        rules_list = [rule for rule in rules.split('\n')]
        final_list = []

        for i in range(1, len(rules_list) - 1):
            rule = command_parser(rules_list[i], i)
            final_list.append(rule)

        return final_list

    @staticmethod
    def Flush():
        result = subprocess.run(
            ['./flushCommand.sh'],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        if result.returncode != 0:
            raise Exception(result.stdout + "\n" + result.stderr)
        return True


