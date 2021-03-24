from insights.core.spec_factory import SpecSet, glob_file
import apicast_logs.models.apicast_logs_constants as const

class ConfigSpecs(SpecSet):
    apicast_log_files_staging = glob_file(const.APICAST_LOGS_PATTERN_STAGING)
    apicast_log_files_production = glob_file(const.APICAST_LOGS_PATTERN_PRODUCTION)
    