#!/usr/bin/python3
# Author:Maweiqing
# -*- coding: utf-8 -*-
# @Time     :2021/2/22 10:30
# @Software: PyCharm
import requests
from common.runmethod import network_process
from common.conf import read_conf,write_cache
from logger import logger
def userinfo():
    logger("获取登录user_id","info")
    login_date = read_conf(config_path="config_test.conf",sec="Userinfo")
    uid = login_date[0][1]
    url = login_date[1][1]
    method = login_date[2][1]
    params = login_date[3][1]
    logger("开始获取cookies","info")
    res = requests.request(url=url,method=method,params=params+"="+uid)
    user_cookies = requests.utils.dict_from_cookiejar(res.cookies)
    logger("拿到cookies","info")
    write_cache(value=user_cookies)
    print(type(res.cookies))
    return res.cookies,user_cookies



if __name__ == "__main__":
    userinfo()