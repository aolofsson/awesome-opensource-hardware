# Use at your own risk!!!!
import os
import re
import sys
import glob

repos = []
# match repos
os.chdir('repos')
with open("../README.md") as f:
    for line in f:
        match = re.search(r'\((https://.*)\)', line)
        if match:
            repos.append(match.group(1))

# clone repos into 'repos'
for name in repos:
    os.system(f"git clone {name}")

# get sizes of all repos
dirs = glob.glob("*")
for name in dirs:
    os.system(f"du -sh {name}")
