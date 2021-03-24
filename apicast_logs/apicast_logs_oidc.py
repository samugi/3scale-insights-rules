from insights.core.plugins import rule, make_pass, make_fail
from apicast_logs.models.apicast_logs_parsers import ApicastLogsCombiner
import apicast_logs.models.apicast_logs_constants as const
import apicast_logs.models.apicast_logs_utils as log_utils

CONTENT = {
    make_fail: "Rule result: [FAILED] "+const.FAILED_CONTENT_LOGS_OIDC,
    make_pass: "Rule result: [PASSED] "+const.PASSED_CONTENT_LOGS_OIDC
}

@rule(ApicastLogsCombiner)
def check_oidc_issuer_endpoints(results):
    failed_staging = []
    passed_staging = []
    failed_production = []
    passed_production = []

    content_staging = results.content_staging
    content_production = results.content_production

    failed_staging, passed_staging = log_utils.evaluate_oidcs(content_staging)
    failed_production, passed_production = log_utils.evaluate_oidcs(content_production)

    if failed_staging or failed_production:
        return make_fail(const.FAIL_KEY, failed_staging=failed_staging, passed_staging=passed_staging, failed_production=failed_production,  passed_production=passed_production)
    return make_pass(const.PASS_KEY, passed_staging=passed_staging, passed_production=passed_production)

