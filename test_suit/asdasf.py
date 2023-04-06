#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

sd = '{"email":"mtbsw5@126.com","email1":"mtbsw51@126.com"}'
sd1 = json.loads(sd)
print(tuple(sd1.items())[0][1])

asd='asd:sdas'
sql_list = asd.split(':')
for i in sql_list:
    print(i)