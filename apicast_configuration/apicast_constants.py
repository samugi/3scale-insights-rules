FAIL_KEY = "APICAST_CONFIG_ERR"
PASS_KEY = "APICAST_CONFIG_OK"

MGMT_API_NOT_ENABLED_STR = "Could not resolve"
CONFIGURATIONS_PATTERN = "*.json"

ERR_ENABLE_MGMT_API = """
APICAST_MANAGEMENT_API must be set to `debug` in APIcast in order to fetch the json configuration from the gateway
"""
FAILED_CONTENT = """

Failed Configs:
{% for m in failed %}    {{m}}
{% endfor %}

Passed Configs:
{% for p in passed_configs %}    {{p}}
{% endfor %}

Ignored Configs:
{% for npc in parsed_configs %}    {{npc}}
{% endfor %}
"""
PASSED_CONTENT = """

Passed Configs:
{% for p in passed_configs %}    {{p}}
{% endfor %}

Ignored Configs:
{% for npc in parsed_configs %}    {{npc}}
{% endfor %}
"""