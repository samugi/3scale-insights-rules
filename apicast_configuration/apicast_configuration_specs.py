from insights.core.spec_factory import SpecSet, glob_file
import apicast_config_check_rules.apicast_constants as const

class ConfigSpecs(SpecSet):
    config_files = glob_file(const.CONFIGURATIONS_PATTERN)