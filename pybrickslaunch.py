HUB_NAME = "Controller3"

import os
import subprocess

target = os.getenv("TARGET")
command = f"pybricksdev run ble --name {HUB_NAME} {target}"

try:
    subprocess.run(command, shell=True, check=True)
except subprocess.CalledProcessError:
    print("Error uploading code to hub")
    print("Make sure the hub is turned on and HUB_NAME is set.")
    
    