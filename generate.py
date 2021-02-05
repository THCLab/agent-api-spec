#!/usr/bin/env python3
import os
import subprocess

path_to_script = os.path.realpath(__file__)
path = os.path.split(path_to_script) 
path_to_spec = path[0] + "/swagger-spec.yaml"
completed = subprocess.run(["swagger-marshmallow-codegen", path_to_spec], capture_output=True)
print(completed.stdout)

print(path[0])
