import re
from urllib.parse import urlparse
import logging
import apicast_logs.models.apicast_logs_constants as const

log = logging.getLogger(__name__)

def some_complex_logic(line):
    return False

def check_errors(log_file):
    error_obj = {}
    for line in log_file:
        error = "some error in APIcast..."
        if some_complex_logic(line):
            error_obj[error] = "    Some hint related to this error"                
    return error_obj

def evaluate_logs(log_file_contents):
    failed = []
    passed = []
    for log_file in log_file_contents:
        log_file_path = log_file.file_path
        log_file_name = log_file.file_name
        log_file_content = log_file.log_content

        errors = check_errors(log_file_content)
        if len(errors) > 0:
            failed.append({'file_name':log_file_path, 'errors': errors})
        else:
            passed.append(log_file_path) 
    return failed, passed