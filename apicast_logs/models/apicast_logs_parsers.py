from insights.core.plugins import parser, combiner
from insights.core import Parser

from apicast_logs.models.apicast_logs_specs import ConfigSpecs

import json
import logging

log = logging.getLogger(__name__)

@parser(ConfigSpecs.apicast_log_files_staging)
class ApicastLogsParserStaging(Parser):
    def parse_content(self, content_staging):
        self.log_content = []
        for log_line in content_staging:
            self.log_content.append(log_line)
        return

@parser(ConfigSpecs.apicast_log_files_production)
class ApicastLogsParserProduction(Parser):
    def parse_content(self, content_production):
        self.log_content = []
        for log_line in content_production:
            self.log_content.append(log_line)
        return

@combiner([ApicastLogsParserStaging, ApicastLogsParserProduction])
class ApicastLogsCombiner(object):
    def __init__(self, log_content_staging, log_content_production):
        if log_content_staging and len(log_content_staging) > 0:
            self.content_staging = log_content_staging
        if log_content_production and len(log_content_production) > 0:
            self.content_production = log_content_production
        else:
            raise SkipComponent(const.ERR_CANT_FIND_LOGS)