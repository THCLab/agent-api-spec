# agent-api-spec
Agent OpenAPI spec

## Requirements

Install requirements.txt

```
pip install -r requirements.txt
```

Install the codegen driver

```
cd codegen_driver
pip install .
```

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

```
python watch_for_changes /home/guy/
```