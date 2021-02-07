import pathlib, time, subprocess, os
# Settings
send_generated_model_to_directory = "/home/sevni/Documents/thclab/aries/aries-cloudagent-python/aries_cloudagent/"

# Script
path_to_script = os.path.realpath(__file__)
path = os.path.split(path_to_script) 
path_to_spec = path[0] + "/swagger-spec.yaml"
path_to_generate_script = path[0] + "/generate.py"

file = pathlib.Path(path_to_spec)
last_mod_time = file.stat().st_mtime
print(last_mod_time)
while 1:
    time.sleep(1)
    mod_time = file.stat().st_mtime
    if last_mod_time != mod_time:
        last_mod_time = mod_time
        print("Generate! ...")
        out = subprocess.run(["python", path_to_generate_script, send_generated_model_to_directory], capture_output=True)
        print(out)
        print("... Done")
    
