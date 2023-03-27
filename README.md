# pp_cmd_pd_merge
Postprocessing command "pd_merge"
## Description
Command uses [pandas merge function](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html) of input dataframe to merge it with subsearch query

### Arguments:
- right - subsearch, subsearch to merge
- how - keyword argument, text, not required, default value is `inner`, type of merge to be performed: left, right, inner, outer, cross
- on - keyword argument, string, required, comma separated fields list

### Usage example:
`... | pd_merge [subsearch query], how='inner', on='field1,field2,field3' `

```
query: readFile a.csv
   a   b
0  1  10
1  2  20
2  3  30
3  4  40
4  5  50

```
```
query: readFile b.csv
   a    c
0  1  100
1  2  200
2  3  300
3  6  600

```
```
query: readFile a.csv | pd_merge [readFile b.csv] on="a", how=inner
1 out of 2 command. Command pd_merge.  Start pd_merge command
   a   b    c
0  1  10  100
1  2  20  200
2  3  30  300
```
```
query: readFile a.csv | pd_merge [readFile b.csv] on="a", how=right
   a     b    c
0  1  10.0  100
1  2  20.0  200
2  3  30.0  300
3  6   NaN  600

```
```
query: readFile a.csv | pd_merge [readFile b.csv] on="a", how=left
1 out of 2 command. Command pd_merge.  Start pd_merge command
   a   b      c
0  1  10  100.0
1  2  20  200.0
2  3  30  300.0
3  4  40    NaN
4  5  50    NaN

```


## Getting started
### Installing
1. Create virtual environment with post-processing sdk 
```bash
    make dev
```
That command  
- downloads [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
- creates python virtual environment with [postprocessing_sdk](https://github.com/ISGNeuroTeam/postprocessing_sdk)
- creates link to current command in postprocessing `pp_cmd` directory 

2. Configure `otl_v1` command. Example:  
```bash
    vi ./venv/lib/python3.9/site-packages/postprocessing_sdk/pp_cmd/otl_v1/config.ini
```
Config example:  
```ini
[spark]
base_address = http://localhost
username = admin
password = 12345678

[caching]
# 24 hours in seconds
login_cache_ttl = 86400
# Command syntax defaults
default_request_cache_ttl = 100
default_job_timeout = 100
```

3. Configure storages for `readFile` and `writeFile` commands:  
```bash
   vi ./venv/lib/python3.9/site-packages/postprocessing_sdk/pp_cmd/readFile/config.ini
   
```
Config example:  
```ini
[storages]
lookups = /opt/otp/lookups
pp_shared = /opt/otp/shared_storage/persistent
```

### Run pd_merge
Use `pp` to run pd_merge command:  
```bash
pp
Storage directory is /tmp/pp_cmd_test/storage
Commmands directory is /tmp/pp_cmd_test/pp_cmd
query: | otl_v1 <# makeresults count=100 #> |  pd_merge 
```
## Deploy
Unpack archive `pp_cmd_pd_merge` to postprocessing commands directory