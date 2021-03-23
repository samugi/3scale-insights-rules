# 3scale-insights-rules
[Red Hat Insights tool](https://www.redhat.com/en/technologies/management/insights) rules to troubleshoot 3scale-must-gather reports.

## Example usage

### Run `apicast_configuration` rules on all the configurations in the must-gather subfolders
```
insights run -p apicast_configuration must-gather.local.12345/
```
### Only check configurations in the selected namespace folder
```
insights run -p apicast_configuration must-gather.local.12345/[...]/apicast-configs/<namespace>/
```
