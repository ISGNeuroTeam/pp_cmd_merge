# pp_cmd_pd_merge
Postprocessing command "pd_merge"
Merge two dataframes using pandas merge function

Arguments:
- right - subsearch, subsearch to merge
- how - text,  type of merge to be performed: left, right, inner, outer, cross
- on - string, comma separated fields list
- copy - boolean, if False, avoid copy if possible.

Usage example:
`... | pd_merge [subsearch query], how='inner', on='field1,field2,field3', copy=True`

## Getting started
###  Prerequisites
1. [Miniconda](https://docs.conda.io/en/latest/miniconda.html)

### Installing
1. Create virtual environment with post-processing sdk 
```bash
make dev
```
That command  
- creates python virtual environment with [postprocessing_sdk](https://github.com/ISGNeuroTeam/postprocessing_sdk)
- creates `pp_cmd` directory with links to available post-processing commands


### Test pd_merge
Use `pp` to test pd_merge command:  
```bash
pp
Storage directory is /tmp/pp_cmd_test/storage
Commmands directory is /tmp/pp_cmd_test/pp_cmd
query: | otl_v1 <# makeresults count=100 #> |  pd_merge 
```
