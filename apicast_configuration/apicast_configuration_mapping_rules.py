from insights.core.plugins import rule, make_pass, make_fail
from apicast_configuration.models.apicast_configuration_parsers import ApicastConfigurationCombiner
import apicast_configuration.models.apicast_configuration_constants as const
import apicast_configuration.models.apicast_configuration_utils as config_utils

CONTENT = {
    make_fail: "Rule result: [FAILED] "+const.FAILED_CONTENT_MAPPING_RULES,
    make_pass: "Rule result: [PASSED] "+const.PASSED_CONTENT
}

@rule(ApicastConfigurationCombiner)
def check_mapping_rules(results):
    nonparsed = []
    passed = []
    failed = {}
    failed = []

    content = results.content
    for result in content:
        configpath = result.file_path
        configname = result.file_name
        config_content = result.config_content
        parsed = result.parsed_config
            
        if not parsed :
            nonparsed.append(configname)
        else:
            failed_rules = config_utils.check_redundant_rules(config_content)
            if len(failed_rules) > 0:
                failed.append({'name':configname, 'failed_rules': failed_rules})
            else:
                passed.append(configname)

    if len(nonparsed) == 0:
        nonparsed.append("[]")

    if failed:
        return make_fail(const.FAIL_KEY, failed=failed, passed_configs=passed, non_parsed_configs=nonparsed)
    return make_pass(const.PASS_KEY, passed_configs=passed, non_parsed_configs=nonparsed)

