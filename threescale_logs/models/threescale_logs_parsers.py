from insights.core.plugins import parser, combiner
from insights.core import Parser

from threescale_logs.models.threescale_logs_specs import ConfigSpecs
import threescale_logs.models.threescale_logs_constants as const

import json
import logging
import re

log = logging.getLogger(__name__)

@parser(ConfigSpecs.threescale_log_files_apicast)
class ThreescaleLogsParserApicast(Parser):
    def parse_content(self, content_production):
        self.log_content = []
        component = re.search(const.COMPONENT_FILTER, self.file_path, re.IGNORECASE)
        self.component = component.group(1) if component else None
        for log_line in content_production:
            self.log_content.append(log_line)
        return

@parser(ConfigSpecs.threescale_log_files_backend_worker)
class ThreescaleLogsParserBackendWorker(Parser):
    def parse_content(self, content_production):
        self.log_content = []
        component = re.search(const.COMPONENT_FILTER, self.file_path, re.IGNORECASE)
        self.component = component.group(1) if component else None
        for log_line in content_production:
            self.log_content.append(log_line)
        return

@parser(ConfigSpecs.threescale_log_files_backend_listener)
class ThreescaleLogsParserBackendListener(Parser):
    def parse_content(self, content_production):
        self.log_content = []
        component = re.search(const.COMPONENT_FILTER, self.file_path, re.IGNORECASE)
        self.component = component.group(1) if component else None
        for log_line in content_production:
            self.log_content.append(log_line)
        return

@parser(ConfigSpecs.threescale_log_files_backend_cron)
class ThreescaleLogsParserBackendCron(Parser):
    def parse_content(self, content_production):
        self.log_content = []
        component = re.search(const.COMPONENT_FILTER, self.file_path, re.IGNORECASE)
        self.component = component.group(1) if component else None
        for log_line in content_production:
            self.log_content.append(log_line)
        return

@parser(ConfigSpecs.threescale_log_files_backend_redis)
class ThreescaleLogsParserBackendRedis(Parser):
    def parse_content(self, content_production):
        self.log_content = []
        component = re.search(const.COMPONENT_FILTER, self.file_path, re.IGNORECASE)
        self.component = component.group(1) if component else None
        for log_line in content_production:
            self.log_content.append(log_line)
        return

@parser(ConfigSpecs.threescale_log_files_system_redis)
class ThreescaleLogsParserSystemRedis(Parser):
    def parse_content(self, content_production):
        self.log_content = []
        component = re.search(const.COMPONENT_FILTER, self.file_path, re.IGNORECASE)
        self.component = component.group(1) if component else None
        for log_line in content_production:
            self.log_content.append(log_line)
        return

@parser(ConfigSpecs.threescale_log_files_system_app)
class ThreescaleLogsParserSystemApp(Parser):
    def parse_content(self, content_production):
        self.log_content = []
        component = re.search(const.COMPONENT_FILTER, self.file_path, re.IGNORECASE)
        self.component = component.group(1) if component else None
        for log_line in content_production:
            self.log_content.append(log_line)
        return

@parser(ConfigSpecs.threescale_log_files_system_sidekiq)
class ThreescaleLogsParserSystemSidekiq(Parser):
    def parse_content(self, content_production):
        self.log_content = []
        component = re.search(const.COMPONENT_FILTER, self.file_path, re.IGNORECASE)
        self.component = component.group(1) if component else None
        for log_line in content_production:
            self.log_content.append(log_line)
        return

@parser(ConfigSpecs.threescale_log_files_system_sphinx)
class ThreescaleLogsParserSystemSphinx(Parser):
    def parse_content(self, content_production):
        self.log_content = []
        component = re.search(const.COMPONENT_FILTER, self.file_path, re.IGNORECASE)
        self.component = component.group(1) if component else None
        for log_line in content_production:
            self.log_content.append(log_line)
        return

@parser(ConfigSpecs.threescale_log_files_system_memcache)
class ThreescaleLogsParserSystemMemcache(Parser):
    def parse_content(self, content_production):
        self.log_content = []
        component = re.search(const.COMPONENT_FILTER, self.file_path, re.IGNORECASE)
        self.component = component.group(1) if component else None
        for log_line in content_production:
            self.log_content.append(log_line)
        return

@parser(ConfigSpecs.threescale_log_files_system_mysql)
class ThreescaleLogsParserSystemMysql(Parser):
    def parse_content(self, content_production):
        self.log_content = []
        component = re.search(const.COMPONENT_FILTER, self.file_path, re.IGNORECASE)
        self.component = component.group(1) if component else None
        for log_line in content_production:
            self.log_content.append(log_line)
        return

@parser(ConfigSpecs.threescale_log_files_zync)
class ThreescaleLogsParserZync(Parser):
    def parse_content(self, content_production):
        self.log_content = []
        component = re.search(const.COMPONENT_FILTER, self.file_path, re.IGNORECASE)
        self.component = component.group(1) if component else None
        for log_line in content_production:
            self.log_content.append(log_line)
        return

@parser(ConfigSpecs.threescale_log_files_zync_database)
class ThreescaleLogsParserZyncDatabase(Parser):
    def parse_content(self, content_production):
        self.log_content = []
        component = re.search(const.COMPONENT_FILTER, self.file_path, re.IGNORECASE)
        self.component = component.group(1) if component else None
        for log_line in content_production:
            self.log_content.append(log_line)
        return

@parser(ConfigSpecs.threescale_log_files_zync_que)
class ThreescaleLogsParserZyncQue(Parser):
    def parse_content(self, content_production):
        self.log_content = []
        component = re.search(const.COMPONENT_FILTER, self.file_path, re.IGNORECASE)
        self.component = component.group(1) if component else None
        for log_line in content_production:
            self.log_content.append(log_line)
        return