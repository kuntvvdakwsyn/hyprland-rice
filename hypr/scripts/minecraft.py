#!/usr/bin/env python3

import subprocess
import time

subprocess.run(["hyprctl","dispatch","workspace","2"])
subprocess.Popen(["discord"])
subprocess.Popen(["firefox","https://aternos.org/server/#goog_rewarded"])

time.sleep(3)

subprocess.run(["hyprctl","dispatch","workspace","1"])
subprocess.Popen(["java","-jar","/home/lain/Downloads/TLauncher.jar"])


