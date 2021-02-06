#!/usr/bin/env python3
import os
import subprocess
import sys

path_to_script = os.path.realpath(__file__)
path = os.path.split(path_to_script) 
path_to_spec = path[0] + "/swagger-spec.yaml"
completed = subprocess.run(["swagger-marshmallow-codegen", path_to_spec], capture_output=True)
generated_output = completed.stdout.decode("utf-8")
generated_output = generated_output.replace("from __future__ import annotations\n", "")

generated_filename = "generated.py"
if len(sys.argv) > 1:
    generated_filename = sys.argv[1] + generated_filename    

f = open(generated_filename, "w")
f.write(generated_output)
f.close()
