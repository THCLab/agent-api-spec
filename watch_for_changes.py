#!/usr/bin/env python3
import pathlib, time, subprocess, os
# Settings
send_generated_model_to_directory = "/home/sevni/Documents/thclab/aries/aries-cloudagent-python/aries_cloudagent/"

# Script
path_to_script = os.path.realpath(__file__)
path = os.path.split(path_to_script) 
path_to_spec = path[0] + "/swagger-spec.yaml"
path_to_generate_script = path[0] + "/generate.py"

file = pathlib.Path(path_to_spec)
generate_script = pathlib.Path(path_to_generate_script)
last_mod_time = file.stat().st_mtime
last_mod_time_generate = generate_script.stat().st_mtime
print(last_mod_time)
while 1:
    time.sleep(1)
    mod_time = file.stat().st_mtime
    mod_time_generate = generate_script.stat().st_mtime
    if last_mod_time != mod_time or last_mod_time_generate != mod_time_generate:
        last_mod_time = mod_time
        last_mod_time_generate = mod_time_generate
        out = subprocess.run(["python", path_to_generate_script, send_generated_model_to_directory], capture_output=True)
        print("STDOUT: ", out.stdout.decode("utf-8"))
        print("STDERROR: ", out.stderr.decode("utf-8"))
    
