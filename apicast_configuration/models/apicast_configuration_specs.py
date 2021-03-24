from insights.core.spec_factory import SpecSet, glob_file
import apicast_configuration.models.apicast_configuration_constants as const

class ConfigSpecs(SpecSet):
    config_files_namespace = glob_file(const.CONFIGURATIONS_PATTERN_NAMESPACE)
    config_files_root = glob_file(const.CONFIGURATIONS_PATTERN_ROOT)
