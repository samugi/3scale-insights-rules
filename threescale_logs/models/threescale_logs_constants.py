FAIL_KEY = "3SCALE_LOGS_ERR"
PASS_KEY = "3SCALE_LOGS_OK"

THREESCALE_LOGS_PATTERN_APICAST_STAGING_PRODUCTION = ["/namespaces/*/pods/apicast-staging-[0-9]*/*apicast*/*apicast*/logs/*.log", "/namespaces/*/pods/apicast-production-[0-9]*/*apicast*/*apicast*/logs/*.log"]
THREESCALE_LOGS_PATTERN_BACKEND_WORKER = "/namespaces/*/pods/backend-worker-[0-9]*/*/*/logs/*.log"
THREESCALE_LOGS_PATTERN_BACKEND_LISTENER = "/namespaces/*/pods/backend-listener-[0-9]*/*/*/logs/*.log"
THREESCALE_LOGS_PATTERN_BACKEND_CRON = "/namespaces/*/pods/backend-cron-[0-9]*/*/*/logs/*.log"
THREESCALE_LOGS_PATTERN_BACKEND_REDIS = "/namespaces/*/pods/backend-redis-[0-9]*/*/*/logs/*.log"
THREESCALE_LOGS_PATTERN_SYSTEM_REDIS = "/namespaces/*/pods/system-redis-[0-9]*/*/*/logs/*.log"
THREESCALE_LOGS_PATTERN_SYSTEM_APP = "/namespaces/*/pods/system-app-[0-9]*/*/*/logs/*.log"
THREESCALE_LOGS_PATTERN_SYSTEM_SIDEKIQ = "/namespaces/*/pods/system-sidekiq-[0-9]*/*/*/logs/*.log"
THREESCALE_LOGS_PATTERN_SYSTEM_SPHINX = "/namespaces/*/pods/system-sphinx-[0-9]*/*/*/logs/*.log"
THREESCALE_LOGS_PATTERN_SYSTEM_MEMCACHE = "/namespaces/*/pods/system-memcache-[0-9]*/*/*/logs/*.log"
THREESCALE_LOGS_PATTERN_SYSTEM_MYSQL = "/namespaces/*/pods/system-mysql-[0-9]*/*/*/logs/*.log"
THREESCALE_LOGS_PATTERN_ZYNC = "/namespaces/*/pods/zync-[0-9]*/*/*/logs/*.log"
THREESCALE_LOGS_PATTERN_ZYNC_DATABASE = "/namespaces/*/pods/zync-database-[0-9]*/*/*/logs/*.log"
THREESCALE_LOGS_PATTERN_ZYNC_QUE = "/namespaces/*/pods/zync-que-[0-9]*/*/*/logs/*.log"
THREESCALE_LOGS_PATTERN_ALL = "/namespaces/*/pods/*/*/*/logs/*.log"

COMPONENT_FILTER = "\/pods\/([a-z0-9]+[-]?[a-z]*)-[0-9]+"

FAILED_CONTENT_LOGS = """

{% for log_file in failed %}
Failed rule for component: [{{log_file.component}}], log file: {{log_file.file_path}}:
{% for error in log_file.errors %}
{{error}}
{% endfor %}
{% endfor %}

{% for p in passed %}
Passed rule for component: [{{p.component}}], log file:  {{p.file_name}}{% endfor %}

"""

PASSED_CONTENT_LOGS = """

{% for p in passed %}
Passed rule for component: {{p.component}}, log file: {{p.file_name}}{% endfor %}

"""