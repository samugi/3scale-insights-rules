import re
from urllib.parse import urlparse
import logging
import apicast_logs.models.apicast_logs_constants as const

log = logging.getLogger(__name__)

def check_issuers(log_file):
    invalid_providers = set()
    for line in log_file:
        if const.ERR_FAILED_OIDC_PROVIDER in line:
            provider = re.search('Provider\sfrom\s(.+?)\s', line)
            invalid_providers.add(provider.group(1))
    return invalid_providers

def evaluate_oidcs(log_file_contents):
    failed = []
    passed = []
    for log_file in log_file_contents:
        log_file_path = log_file.file_path
        log_file_name = log_file.file_name
        log_file_content = log_file.log_content

        invalid_issuers = check_issuers(log_file_content)
        if len(invalid_issuers) > 0:
            failed.append({'name':log_file_path, 'invalid_issuers': invalid_issuers})
        else:
            passed.append(log_file_path) 
    return failed, passed