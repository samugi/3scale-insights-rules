#parsers are called once for every config file in the glob_file (defined in apicast_configuration_specs)
#and result in a list of objects that is then selected by the combiner

from insights.core.plugins import parser, combiner
from insights.core import Parser
from insights.core.dr import SkipComponent

from apicast_configuration.models.apicast_configuration_specs import ConfigSpecs
import apicast_configuration.models.apicast_configuration_constants as const
import apicast_configuration.models.apicast_configuration_utils as config_utils

import json
import logging

log = logging.getLogger(__name__)

def parse_configs(self, content): 
    self.parsed_config = True
        
    config_lines = []
    for line in content :
        config_lines.append(line)
    raw_config = "\n".join(config_lines)

    if const.MGMT_API_NOT_ENABLED_STR in raw_config :
        log.error(f"{const.ERR_ENABLE_MGMT_API}")
        self.parsed_config = False
        self.config_content = raw_config
    else : 
        self.config_content = config_utils.normalize_config(json.loads(raw_config))
    return

#parse apicast configurations from the namespace folder
@parser(ConfigSpecs.config_files_namespace)
class ApicastConfigurationNSParser(Parser):
    def parse_content(self, content):
        return parse_configs(self, content)

#parse apicast configurations from the root folder of must-gather
@parser(ConfigSpecs.config_files_root)
class ApicastConfigurationRootParser(Parser):
    def parse_content(self, content):
        return parse_configs(self, content)

@combiner([ApicastConfigurationNSParser, ApicastConfigurationRootParser])
class ApicastConfigurationCombiner(object):
    def __init__(self, content_namespace, content_root):
        if content_root and len(content_root) > 0:
            self.content = content_root
        elif content_namespace and len(content_namespace) > 0:
            self.content = content_namespace
        else:
            raise SkipComponent(const.ERR_CANT_FIND_CONFIGS)