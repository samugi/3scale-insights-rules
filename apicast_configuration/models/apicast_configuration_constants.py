FAIL_KEY = "APICAST_CONFIG_ERR"
PASS_KEY = "APICAST_CONFIG_OK"

MGMT_API_NOT_ENABLED_STR = "Could not resolve"
CONFIGURATIONS_PATTERN_NAMESPACE = "*.json"
CONFIGURATIONS_PATTERN_ROOT = "/apicast-configs/*/*.json"

ERR_ENABLE_MGMT_API = """
APICAST_MANAGEMENT_API must be set to `debug` in APIcast in order to fetch the json configuration from the gateway
"""
ERR_CANT_FIND_CONFIGS = "Unable to find APIcast configurations in the provided path."

FAILED_CONTENT_MAPPING_RULES = """
Incompatible mapping rules detected: 
{% for config in failed %}
Checks failed for config {{config.name}} for the following mapping rules:
{% for rules in config.failed_rules %}
    id={{rules[0]['id']}}, pattern={{rules[0]['pattern']}}, service={{rules[0]['proxy_id']}}, host={{rules[0]['host']}}
    id={{rules[1]['id']}}, pattern={{rules[1]['pattern']}}, service={{rules[1]['proxy_id']}}, host={{rules[1]['host']}}
{% endfor %}
{% endfor %}

Passed Configs:
{% for p in passed_configs %}    {{p}}
{% endfor %}

Ignored Configs:
{% for npc in non_parsed_configs %}    {{npc}}
{% endfor %}
"""

PASSED_CONTENT = """

Passed Configs:
{% for p in passed_configs %}    {{p}}
{% endfor %}

Ignored Configs:
{% for npc in non_parsed_configs %}    {{npc}}
{% endfor %}
"""