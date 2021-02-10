# agent-api-spec
Agent OpenAPI spec

## How to generate models 

This command will generate models to current folder:
```
./generate.py
```

You can pass the output folder to the script (Make sure to put '/' at the end)
```
./generate.py /home/guy/
```


## Filewatcher

This script watches both the spec and generate script for changes. Calls generate.py on changes.
Path to the output folder is specified using a variable in the script. You need to edit
the script to change it.
