import yaml

f = open("swagger-spec.yaml", "r")
content = f.read()
content = yaml.safe_load(content)
print(content['paths'].keys())
