#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
# 把当前文件所在文件夹的父文件夹路径加入到PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import requests,random
from common.log import Logger
from config.config_data import ip

log = Logger(__name__).get_logger()


class DoRequest():
    def __init__(self):
        pass

    def get_url(self, url, **par):
        # url : /app/runActivity/startRun
        try:
            url = 'http://'+ ip+ url
            res = requests.get(url, **par)
        except Exception:
            log.exception('error！ url:%s,par:%s ' % (url, par))
        else:
            log.info('get url:%s,par:%s succeed!,response = %s' % (url, par,res.text))
            return res

    def post_url(self, url, json=None, **kwargs):
        # url : /app/runActivity/startRun
        try:
            url = 'http://'+ip + url
            res = requests.post(url, json=json, **kwargs)

        except Exception:
            log.exception('error！ url:%s,data:%s ' % (url, json))
        else:
            log.info('get url:%s,par:%s succeed! ,response = %s' % (url, json,res.text))
            return res


if __name__ == '__main__':
    res1 = DoRequest().post_url('/app/runActivity/startRun',
                                json={"activityId": 24599, "challengeRank": 4, "challengedUserId": 63353, "pageNum": 1,
                                      "pageSize": 10},
                                headers={"email": "mtbsw5@126.com", "Content-Type": "application/json"})
    print(res1)
    rint = random.randint(100,999)
    run_data = {"activityId": 24599, "data": [
        {"calories": 68, "gradient": 0, "heartRate": 0, "mileage": 823, "runTime": 241977, "stepNum": 0,
         "velocity": 15000},
        {"calories": 68, "gradient": 0, "heartRate": 0, "mileage": 827, "runTime": 242977, "stepNum": 0,
         "velocity": 15000},
        {"calories": 68, "gradient": 0, "heartRate": 0, "mileage": 831, "runTime": 243977, "stepNum": 0,
         "velocity": 15000},
        {"calories": 69, "gradient": 0, "heartRate": 0, "mileage": 835, "runTime": 244977, "stepNum": 0,
         "velocity": 15000},
        {"calories": 69, "gradient": 0, "heartRate": 0, "mileage": 839, "runTime": 245977, "stepNum": 0,
         "velocity": 15000},
        {"calories": 69, "gradient": 0, "heartRate": 0, "mileage": 843, "runTime": 246977, "stepNum": 0,
         "velocity": 15000},
        {"calories": 70, "gradient": 0, "heartRate": 0, "mileage": 848, "runTime": 247977, "stepNum": 0,
         "velocity": 15000},
        {"calories": 70, "gradient": 0, "heartRate": 0, "mileage": 852, "runTime": 248977, "stepNum": 0,
         "velocity": 15000},
        {"calories": 70, "gradient": 0, "heartRate": 0, "mileage": 856, "runTime": 249977, "stepNum": 0,
         "velocity": 15000},
        {"calories": 71, "gradient": 0, "heartRate": 0, "mileage": 860, "runTime": 250977, "stepNum": 0,
         "velocity": 15000},
        {"calories": 71, "gradient": 0, "heartRate": 0, "mileage": 864, "runTime": 251977, "stepNum": 0,
         "velocity": 15000},
        {"calories": 72, "gradient": 0, "heartRate": 0, "mileage": 868, "runTime": 252977, "stepNum": 0,
         "velocity": 15000},
        {"calories": 72, "gradient": 0, "heartRate": 0, "mileage": 873, "runTime": 253977, "stepNum": 0,
         "velocity": 15000},
        {"calories": 72, "gradient": 0, "heartRate": 0, "mileage": 877, "runTime": 254977, "stepNum": 0,
         "velocity": 15000},
        {"calories": 73, "gradient": 0, "heartRate": 0, "mileage": 881, "runTime": 255977, "stepNum": 0,
         "velocity": 15000},
        {"calories": 73, "gradient": 0, "heartRate": 0, "mileage": 885, "runTime": 256977, "stepNum": 0,
         "velocity": 15000},
        {"calories": 73, "gradient": 0, "heartRate": 0, "mileage": 889, "runTime": 257977, "stepNum": 0,
         "velocity": 15000},
        {"calories": 74, "gradient": 0, "heartRate": 0, "mileage": 893, "runTime": 258977, "stepNum": 0,
         "velocity": 15000},
        {"calories": 74, "gradient": 0, "heartRate": 0, "mileage": 898, "runTime": 259977, "stepNum": 0,
         "velocity": 15000},
        {"calories": 74, "gradient": 0, "heartRate": 0, "mileage": 902, "runTime": 260977, "stepNum": 0,
         "velocity": 15000},
        {"calories": 75, "gradient": 0, "heartRate": 0, "mileage": 906, "runTime": 261977, "stepNum": 0,
         "velocity": 15000},
        {"calories": 75, "gradient": 0, "heartRate": 0, "mileage": 910, "runTime": 262977, "stepNum": 0,
         "velocity": 15000},
        {"calories": 75, "gradient": 0, "heartRate": 0, "mileage": 914, "runTime": 263977, "stepNum": 0,
         "velocity": 15000},
        {"calories": 76, "gradient": 0, "heartRate": 0, "mileage": 918, "runTime": 264977, "stepNum": 0,
         "velocity": 15000},
        {"calories": 76, "gradient": 0, "heartRate": 0, "mileage": 923, "runTime": 265977, "stepNum": 0,
         "velocity": 15000},
        {"calories": 76, "gradient": 0, "heartRate": 0, "mileage": 927, "runTime": 266977, "stepNum": 0,
         "velocity": 15000},
        {"calories": 77, "gradient": 0, "heartRate": 0, "mileage": 931, "runTime": 267977, "stepNum": 0,
         "velocity": 15000},
        {"calories": 77, "gradient": 0, "heartRate": 0, "mileage": 935, "runTime": 268977, "stepNum": 0,
         "velocity": 15000},
        {"calories": 77, "gradient": 0, "heartRate": 0, "mileage": 939, "runTime": 269977, "stepNum": 0,
         "velocity": 15000},
        {"calories": 78, "gradient": 0, "heartRate": 0, "mileage": 943, "runTime": 270977, "stepNum": 0,
         "velocity": 15000},
        {"calories": 78, "gradient": 0, "heartRate": 0, "mileage": 948, "runTime": 271977, "stepNum": 0,
         "velocity": 15000},
        {"calories": 78, "gradient": 0, "heartRate": 0, "mileage": 952, "runTime": 272977, "stepNum": 0,
         "velocity": 15000},
        {"calories": 79, "gradient": 0, "heartRate": 0, "mileage": 956, "runTime": 273977, "stepNum": 0,
         "velocity": 15000},
        {"calories": 79, "gradient": 0, "heartRate": 0, "mileage": 960, "runTime": 274977, "stepNum": 0,
         "velocity": 15000},
        {"calories": 79, "gradient": 0, "heartRate": 0, "mileage": 964, "runTime": 275977, "stepNum": 0,
         "velocity": 15000},
        {"calories": 80, "gradient": 0, "heartRate": 0, "mileage": 968, "runTime": 276977, "stepNum": 0,
         "velocity": 15000},
        {"calories": 80, "gradient": 0, "heartRate": 0, "mileage": 973, "runTime": 277977, "stepNum": 0,
         "velocity": 15000},
        {"calories": 80, "gradient": 0, "heartRate": 0, "mileage": 977, "runTime": 278977, "stepNum": 0,
         "velocity": 15000},
        {"calories": 81, "gradient": 0, "heartRate": 0, "mileage": 981, "runTime": 279977, "stepNum": 0,
         "velocity": 15000},
        {"calories": 81, "gradient": 0, "heartRate": 0, "mileage": 985, "runTime": 280977, "stepNum": 0,
         "velocity": 15000},
        {"calories": 82, "gradient": 0, "heartRate": 0, "mileage": 989, "runTime": 281977, "stepNum": 0,
         "velocity": 15000},
        {"calories": 82, "gradient": 0, "heartRate": 0, "mileage": 993, "runTime": 282977, "stepNum": 0,
         "velocity": 15000},
        {"calories": 83, "gradient": 0, "heartRate": 0, "mileage": 1000, "runTime": 283978, "stepNum": 0,
         "velocity": 14500}], "distanceTarget": 1000, "firmwareVersion": 23, "id_no": 345, "order_no": rint,
                "routeId": 101, "run_status": 1, "timeTarget": -1, "unique_code": "MQmq58CF791677A\u0000"}
    res2 = DoRequest().post_url('/app/equipment/data', json=run_data,headers ={"email": "mtbsw5@126.com", "Content-Type": "application/json"} )
    print(res2)
    print(res2.text)
