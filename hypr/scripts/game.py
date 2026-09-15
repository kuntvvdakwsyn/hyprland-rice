#!/usr/bin/env python3
import time
import subprocess

subprocess.run(["hyprctl","dispatch","workspace","2"])
subprocess.Popen(["steam"])
subprocess.Popen(["discord"])
