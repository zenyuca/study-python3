#!/usr/bin/env python3
# _*_ encoding=utf-8 _*_
import json


class Base(object):

    # 将对象属性转换成 JSON
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
