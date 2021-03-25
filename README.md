# 3scale-insights-rules
[Red Hat Insights](https://github.com/RedHatInsights/insights-core) rules to troubleshoot 3scale-must-gather reports.

## Examples of usage

### Run `apicast_configuration` rules on all the configurations in the must-gather subfolders
```
insights run -p apicast_configuration must-gather.local.12345/
```
### Only check configurations in the selected namespace folder
```
insights run -p apicast_configuration must-gather.local.12345/[...]/apicast-configs/<namespace>/
```
### Run APIcast logs rules on all APIcast logs
```
insights run -p threescale_logs.threescale_logs_apicast must-gather.local.12345/
```
### Run all logs rules at once
```
insights run -p threescale_logs must-gather.local.12345/
```

## Error mappings
Rules in the `threescale_logs` folder use a simple logic where every error has a comment associated. If at least one error is found in the files scanned by the rule, the rule will fail and the comment will be printed in the output. The `error -> comment` mapping is configured in `threescale_logs/models/threescale_error_mappings.py`: Regex syntax can be used to assign values to the parameters in the comment. The regex is intended to match from the same log line where the error was detected (see the example below). Every error definition object should be placed within the list named as the component it refers to.

### Example
Given the following log line:
```
[error] 20#20: *3318 discovery.lua:108: openid_configuration(): failed to get OIDC Provider from https://example.org/.well-known/openid-configuration status: 404
```
This error definition:
```
{
    'error_trigger':"failed to get OIDC Provider",
    'message':{
        'pattern': "    [error] Invalid provider issuer: [{issuer}] check connectivity between APIcast and \"{host}\"",
        'params':{
            'issuer':"Provider\sfrom\s(.+?)\s",
            'host':"Provider\sfrom\s(http[s]:\/\/*.*?)[\/]"
        }
    }
}
```
Detects the log line based on the `error_trigger` field, then makes the rule fail with the following output:
```
[error] Invalid provider issuer: [https://example.org/.well-known/openid-configuration] check connectivity between APIcast and "https://example.org"
```