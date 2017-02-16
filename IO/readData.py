#!/usr/bin/env python3
# _*_ encoding=utf-8 _*_

import json


def readData():
    with open('./data.json', 'r') as f:
        json_str = f.read()
        d = json.loads(json_str)
        return d

d = readData()
print(d['seller'])
