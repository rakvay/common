#!/usr/bin/env python3

import os

import base64

print(base64.b64encode(os.urandom(64)).decode('utf-8'))
