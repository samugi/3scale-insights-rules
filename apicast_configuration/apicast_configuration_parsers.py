from insights.core.plugins import parser
from insights.core import Parser
from apicast_config_check_rules.apicast_configuration_specs import ConfigSpecs
import apicast_config_check_rules.apicast_constants as const
import apicast_config_check_rules.apicast_configuration_utils as config_utils
import json

#parse_content is called once for every file in the glob_file object
@parser(ConfigSpecs.config_files)
class ApicastConfiguration(Parser):
    def parse_content(self, content):
        self.parsed_config = True
        for config in content :
            if const.MGMT_API_NOT_ENABLED_STR in config :
                print(const.ERR_ENABLE_MGMT_API)
                self.parsed_config = False
                self.config_content = config
            else : 
                self.config_content = config_utils.normalize_config(json.loads(config))
        return