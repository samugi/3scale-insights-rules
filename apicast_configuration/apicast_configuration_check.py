from insights.core.plugins import rule, make_pass, make_fail
from apicast_config_check_rules.apicast_configuration_parsers import ApicastConfiguration
import apicast_config_check_rules.apicast_constants as const
import apicast_config_check_rules.apicast_configuration_utils as config_utils

CONTENT = {
    make_fail: "Rule result: [FAILED] "+const.FAILED_CONTENT,
    make_pass: "Rule result: [PASSED] "+const.PASSED_CONTENT
}

@rule(ApicastConfiguration)
def check_oidc_issuer_endpoints(results):
    failed = []
    passed = []
    nonparsed = []

    # each result is an ApicastConfiguration object, 
    # one for each configuration file from the glob_files
    for result in results:
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

