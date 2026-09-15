#!/usr/bin/env python3

import subprocess
import time

subprocess.run(["hyprctl","dispatch","workspace","1"])
subprocess.Popen(["firefox","https://soundcloud.com","https://gemini.google.com"])

time.sleep(1)

subprocess.run(["hyprctl","dispatch","workspace","2"])
subprocess.Popen(["viber"])
