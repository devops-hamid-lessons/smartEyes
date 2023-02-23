import parse

ACTIONS = {
    0: "ACCEPT",
    1: "DROP"
}

CHAINS = {
    0: "INPUT",
    1: "OUTPUT",
    2: "FORWARD"
}

def command_parser(rule_item, index):
    rule = {'index_rule_id': index}

    chain = parse.search('-A {:w} ', rule_item)
    if chain is not None:
        rule['chain'] = chain.fixed[0]

    source = parse.search('-s {} ', rule_item)
    if source is not None:
        rule['source'] = source.fixed[0]

    destination = parse.search('-d {} ', rule_item)
    if destination is not None:
        rule['destination'] = destination.fixed[0]

    protocol = parse.search(' -p {:w} ', rule_item)
    if protocol is not None:
        rule['protocol'] = protocol.fixed[0]

    destination_port = parse.search(' --dport {:w} ', rule_item)
    if destination_port is not None:
        rule['dport'] = int(destination_port.fixed[0])

    source_port = parse.search(' --sport {:w} ', rule_item)
    if source_port is not None:
        rule['sport'] = int(source_port.fixed[0])

    action = parse.search(' -j {:w}', rule_item)
    if action is not None:
        rule['action'] = action.fixed[0]

    rule_id = parse.search('--comment {} ', rule_item)
    if rule_id is not None:
        rule['rule_id'] = rule_id.fixed[0]

    return rule


