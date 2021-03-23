from insights.core.plugins import rule, make_pass, make_fail
from apicast_configuration.models.apicast_configuration_parsers import ApicastConfigurationCombiner
import apicast_configuration.models.apicast_constants as const
import apicast_configuration.models.apicast_configuration_utils as config_utils

CONTENT = {
    make_fail: "Rule result: [FAILED] "+const.FAILED_CONTENT,
    make_pass: "Rule result: [PASSED] "+const.PASSED_CONTENT
}

@rule(ApicastConfigurationCombiner)
def check_oidc_issuer_endpoints(results):
    failed = []
    passed = []
    nonparsed = []

    content = results.content
    for result in content:
        configpath = result.file_path
        configname = result.file_name
        config_content = result.config_content
        parsed = result.parsed_config
            
        if not parsed :
            nonparsed.append(configname)
        elif not config_utils.check_issuers(config_content):
            failed.append(configname)
        else :
            passed.append(configname) 

    if len(nonparsed) == 0:
        nonparsed.append("[]")

    if failed:
        return make_fail(const.FAIL_KEY, failed=failed, passed_configs=passed, parsed_configs=nonparsed)
    return make_pass(const.PASS_KEY, passed_configs=passed, parsed_configs=nonparsed)

