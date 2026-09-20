#!/usr/bin/env python3

import subprocess
import time

subprocess.run(["hyprctl","dispatch","workspace","1"])
subprocess.Popen("evince")
time.sleep(0.7)
subprocess.run(["hyprctl","dispatch","workspace","3"])
subprocess.Popen(["firefox","https://soundcloud.com","https://gemini.google.com","https://claude.ai"])
time.sleep(0.7)
subprocess.run(["hyprctl","dispatch","workspace","2"])
subprocess.Popen("obsidian")
