FAIL_KEY = "APICAST_LOGS_ERR"
PASS_KEY = "APICAST_LOGS_OK"

ERR_FAILED_OIDC_PROVIDER = "failed to get OIDC Provider"

ERR_CANT_FIND_LOGS = "Unable to find logs in the selected path"

APICAST_LOGS_PATTERN_STAGING = "/namespaces/*/pods/apicast-staging*/*apicast*/*apicast*/logs/*.log"
APICAST_LOGS_PATTERN_PRODUCTION = "/namespaces/*/pods/apicast-production*/*apicast*/*apicast*/logs/*.log"

FAILED_CONTENT_LOGS_OIDC = """

Failed STAGING log files:
{% for log_file in failed_staging %}
    {{log_file.file_name}}:
{% for error in log_file.errors %}
{{log_file.errors[error]}}
{% endfor %}
{% endfor %}

Passed STAGING log files:
{% for p in passed_staging %}    {{p}}
{% endfor %}

Failed PRODUCTION log files:
{% for log_file in failed_production %}
    {{log_file.file_name}}:
{% for error in log_file.errors %}
{{log_file.errors[error]}}
{% endfor %}
{% endfor %}

Passed PRODUCTION log files:
{% for p in passed_production %}    {{p}}
{% endfor %}

"""

PASSED_CONTENT_LOGS_OIDC = """

Passed STAGING Logfiles:
{% for p in passed_staging %}    {{p}}
{% endfor %}

Passed PRODUCTION Logfiles:
{% for p in passed_production %}    {{p}}
{% endfor %}

"""