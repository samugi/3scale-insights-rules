from insights.core.plugins import rule, make_pass, make_fail
from threescale_logs.models.threescale_logs_parsers import *
import threescale_logs.models.threescale_logs_constants as const
import threescale_logs.models.threescale_logs_utils as log_utils

CONTENT = {
    make_fail: "Rule result: [FAILED] "+const.FAILED_CONTENT_LOGS,
    make_pass: "Rule result: [PASSED] "+const.PASSED_CONTENT_LOGS
}

@rule(ThreescaleLogsParserBackendRedis)
def check_standard_logs_backend_redis(content):
    failed= []
    passed = []

    failed, passed = log_utils.evaluate_logs(content)

    if failed:
        return make_fail(const.FAIL_KEY, failed=failed, passed=passed)
    return make_pass(const.PASS_KEY, passed=passed)

@rule(ThreescaleLogsParserSystemRedis)
def check_standard_logs_system_redis(content):
    failed= []
    passed = []

    failed, passed = log_utils.evaluate_logs(content)

    if failed:
        return make_fail(const.FAIL_KEY, failed=failed, passed=passed)
    return make_pass(const.PASS_KEY, passed=passed)
