#!/usr/bin/env python3

import os

cur_dir = os.getcwd()
print("Current working directory is:", cur_dir)

print("Absolute path + current folder:", os.path.split(cur_dir))

print("Path:", os.path.dirname(cur_dir))

print("Current folder:", os.path.basename(cur_dir))

print("***Show folder's tree***")
while os.path.basename(cur_dir):
    cur_dir = os.path.dirname(cur_dir)
    print(cur_dir)
