import re
from urllib.parse import urlparse

def check_issuers(config):
    for service in config['services'] :
        proxy = service['proxy']
        is_oidc = True if proxy['authentication_method'] == "oidc" else False
        if is_oidc and not validate_issuer(proxy['oidc_issuer_endpoint'], proxy['oidc_issuer_type']) : 
            return False
    return True

def validate_issuer(iss, type):
    parsed = urlparse(iss)
    scheme = parsed.scheme
    netloc = parsed.netloc
    # path = parsed.path
    netloc_ok = netloc != '' if type != "keycloak" else re.match(".+:.+@.+", netloc)
    return scheme != '' and netloc_ok

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