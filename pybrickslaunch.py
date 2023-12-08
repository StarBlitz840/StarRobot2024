HUB_NAME = "Controller4"

import os
import subprocess

target = os.getenv("TARGET")
command = f"pybricksdev run ble --name {HUB_NAME} {target}"

try:
    subprocess.run(command, shell=True, check=True)
except subprocess.CalledProcessError:
    print("beep boop boop beep")
    print("Error uploading code to hub")
    