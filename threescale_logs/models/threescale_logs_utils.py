import re
from urllib.parse import urlparse
import logging
import threescale_logs.models.threescale_logs_constants as const
import threescale_logs.models.threescale_error_mappings as error_mappings

log = logging.getLogger(__name__)

def re_search(param, line):
    match = re.search(param,line) if param else None
    return match.group(1) if match and match.lastindex else None


def regexify_params(fparams, line):
    params = {}
    for k, v in fparams.items():
        if v :
            params[k] = re_search(v, line)
    return params

def check_errors(component, log_file):
    error_obj = set()
    error_map = error_mappings.ERROR_MAPPINGS
    if component in error_map:
        for line in log_file:
            for error_def in error_map[component]:
                if error_def["error_trigger"] in line:
                    fmessage = error_def["message"]["pattern"]
                    fparams = regexify_params(error_def["message"]["params"], line)

                    message = fmessage.format(**fparams)
                    error_obj.add(message)
    return error_obj

def evaluate_logs(log_file_contents):
    failed = []
    passed = set()
    for log_file in log_file_contents:
        log_file_path = log_file.file_path
        log_file_name = log_file.file_name
        log_file_content = log_file.log_content
        log_file_component = log_file.component
        log_file.errors = check_errors(log_file_component, log_file_content)
        if len(log_file.errors) > 0:
            failed.append(log_file)
        else:
            passed.add(log_file) 
    return failed, passed