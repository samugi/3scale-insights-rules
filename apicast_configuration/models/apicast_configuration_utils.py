import re
from urllib.parse import urlparse
import logging

log = logging.getLogger(__name__)

#turns every configuration format in a list of services
def normalize_config(raw_config):
    if "services" in raw_config:
        return raw_config
    if "proxy_configs" in raw_config:
        config = {}
        config["services"] = []
        for proxy_config in raw_config["proxy_configs"]:
            config["services"].append(proxy_config["proxy_config"]["content"])
        return config
    return None

def get_rules_by_host(config):
    rules_by_host = {}
    for service in config["services"]:
        proxy = service["proxy"]
        for mapping_rule in proxy["proxy_rules"]:
            host = proxy["endpoint"]
            if not host or host == "":
                host = proxy["sandbox_endpoint"]
            if host not in rules_by_host:
                rules_by_host[host] = []
            mapping_rule["host"] = host
            rules_by_host[host].append(mapping_rule)
    return rules_by_host

def replace_params(pattern):
    return re.sub("{.*}","#", pattern)

def patterns_match(p1, p2):
    longer = p1 if len(p1) > len(p2) else p2
    shorter = p2 if p1 == longer else p1
    longer = replace_params(longer)
    shorter = replace_params(shorter)

    if len(longer) > len(shorter):
        if shorter.endswith("$") and not longer.endswith("$"):
            shorter = shorter.split("$")[0]
        elif longer.endswith("$"):
            return False

    return longer.startswith(shorter) 

def patterns_equal(p1, p2):
    p1 = replace_params(p1)
    p2 = replace_params(p2)
    return p1.split("$")[0] == p2.split("$")[0]

def rules_are_similar(rule1, rule2):
    method1 = rule1["http_method"]
    owner_type1 = rule1["owner_type"]
    pattern1 = rule1["pattern"].split("?")[0]
    qp1 = rule1["querystring_parameters"] if "querystring_parameters" in rule1 else {}
    method2 = rule2["http_method"]
    owner_type2 = rule2["owner_type"]
    pattern2 = rule2["pattern"].split("?")[0]
    qp2 = rule2["querystring_parameters"] if "querystring_parameters" in rule2 else {}
    return method1 == method2 and owner_type1 == owner_type2 and patterns_match(pattern1, pattern2) and qp1 == qp2

# returns True if these rules are incompatible
# provided the rules are from services with the same host (see check_redundant_rules)
def rules_are_incompatible(rule1, rule2):
    owner_id1 = rule1["owner_id"]
    owner_id2 = rule2["owner_id"]
    return rules_are_similar(rule1, rule2) and owner_id1 != owner_id2

# returns True if these rules are redundant
# provided the rules are from services with the same host (see check_redundant_rules)
def rules_are_redundant(rule1, rule2):
    metric1 = rule1["metric_id"]
    metric2 = rule2["metric_id"]
    return rules_are_similar(rule1, rule2) and metric1 == metric2

# looks for unnecessary mapping rules (duplicate or matching with same metrics)
# here we only compare rules that have the same host (same service or different services w/ path based routing)
# returns a list of invalid rules (incompatible). 
# Logs warnings for harmless but questionable mapping rules (redundant)
def check_redundant_rules(config):
    rules_by_host = get_rules_by_host(config)
    incompatible_rules = []
    for rulehost in rules_by_host:
        for rule1 in rules_by_host[rulehost]:
            rules_by_host[rulehost].remove(rule1)
            for rule2 in rules_by_host[rulehost]:
                if rules_are_incompatible(rule1, rule2):
                    incompatible_rules.append([rule1, rule2])
                elif rules_are_redundant(rule1, rule2):
                    log.warn(f"\nRedundant mapping rules detected: \nid={rule1['id']}, pattern={rule1['pattern']}, service={rule1['proxy_id']}, host={rule1['host']}\nid={rule2['id']}, pattern={rule2['pattern']}, service={rule2['proxy_id']}, host={rule2['host']}")
    return incompatible_rules