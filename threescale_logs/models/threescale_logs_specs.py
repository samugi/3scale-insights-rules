from insights.core.spec_factory import SpecSet, glob_file
import threescale_logs.models.threescale_logs_constants as const

class ConfigSpecs(SpecSet):
    #threescale_log_files = glob_file(const.THREESCALE_LOGS_PATTERN_ALL)
    threescale_log_files_apicast = glob_file(const.THREESCALE_LOGS_PATTERN_APICAST_STAGING_PRODUCTION)
    threescale_log_files_backend_worker = glob_file(const.THREESCALE_LOGS_PATTERN_BACKEND_WORKER)
    threescale_log_files_backend_listener = glob_file(const.THREESCALE_LOGS_PATTERN_BACKEND_LISTENER)
    threescale_log_files_backend_cron = glob_file(const.THREESCALE_LOGS_PATTERN_BACKEND_CRON)
    threescale_log_files_backend_redis = glob_file(const.THREESCALE_LOGS_PATTERN_BACKEND_REDIS)
    threescale_log_files_system_redis = glob_file(const.THREESCALE_LOGS_PATTERN_SYSTEM_REDIS)
    threescale_log_files_system_app = glob_file(const.THREESCALE_LOGS_PATTERN_SYSTEM_APP)
    threescale_log_files_system_sidekiq = glob_file(const.THREESCALE_LOGS_PATTERN_SYSTEM_SIDEKIQ)
    threescale_log_files_system_sphinx = glob_file(const.THREESCALE_LOGS_PATTERN_SYSTEM_SPHINX)
    threescale_log_files_system_memcache = glob_file(const.THREESCALE_LOGS_PATTERN_SYSTEM_MEMCACHE)
    threescale_log_files_system_mysql = glob_file(const.THREESCALE_LOGS_PATTERN_SYSTEM_MYSQL)
    threescale_log_files_zync = glob_file(const.THREESCALE_LOGS_PATTERN_ZYNC)
    threescale_log_files_zync_database = glob_file(const.THREESCALE_LOGS_PATTERN_ZYNC_DATABASE)
    threescale_log_files_zync_que = glob_file(const.THREESCALE_LOGS_PATTERN_ZYNC_QUE)
