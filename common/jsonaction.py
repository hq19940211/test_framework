#!/usr/bin/python3
# Author:Maweiqing
# -*- coding: utf-8 -*-
# @Time     :2021/2/22 10:29
# @Software: PyCharm
import json
from common.logger import logger

def openjson(filename,json_name="",date_type=""):
    '''
    :param filename: json文件名
    :param json_name: 文件中json名
    :param date_type: json中数据中需要的字段
    :return:返回数据
    '''
    json_file_path = "test_data/"
    with open(json_file_path+filename+".json",'r',encoding="utf-8") as f:
        if date_type != "" and json_name != "":
            f = json.load(f)[json_name][date_type]

        elif json_name != "" and date_type == "":
            f = json.load(f)[json_name]

        elif json_name == "" and date_type != "":
            logger("json中数据中需要的字段需要传入文件中json名","WARNING")

        else:
            f = json.load(f)
        return f

def writejson():
    pass


if __name__ == "__main__":
    print(openjson("login-1","case1","data"))