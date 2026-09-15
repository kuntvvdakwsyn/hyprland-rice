#!/usr/bin/env python3
import subprocess
import time

subprocess.run(["hyprctl","dispatch","workspace","1"])
subprocess.Popen(["foot","-e","nvim"])

time.sleep(0.5)

subprocess.run(["hyprctl","dispatch","workspace","2"])
subprocess.Popen(["firefox","https://soundcloud.com","https://github.com/","https://gemini.google.com","https://claude.ai","https://chatgpt.com"])
