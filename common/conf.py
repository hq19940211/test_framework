#!/usr/bin/python3
# Author:Maweiqing
# -*- coding: utf-8 -*-
# @Time     :2021/2/22 10:29
# @Software: PyCharm
import configparser
from common import runmethod
from common.logger import logger
import configobj

def read_conf(sec="",opts="",config_path=""):
    '''
    :param sec: conf中的section
    :param opts:conf中的section的键
    :param config_path:日志的地址
    :return:查到的数据
    '''
    if config_path !="":
        conf = configparser.ConfigParser()
        conf.read(config_path,encoding="utf-8")
        if sec != "" and opts != "":
            kvs = conf.get(section=sec,option=opts)
        elif sec == "" and opts == "":
            logger("查询没传递section和option","WARNING")
        else:
            kvs = conf.items(sec)
        return kvs
    else:
        logger("查询没传日志的地址","WARNING")


def write_cache1(opts="",value="",cache_path="catch.ini",sec="CACHE"):
    conf =configparser.ConfigParser()
    if not conf.has_section(sec):
        conf.add_section(sec)
    conf.read(cache_path, encoding="utf-8")
    conf.set(sec,opts,value)
    with open(cache_path,'w',encoding="utf-8") as f:
        conf.write(f)


def write_cache(opts="",value="",cache_path="catch.ini",sec="CACHE"):
    '''
    :param sec: conf中的section
    :param opts:缓存的键
    :param cache_path:缓存的地址
    :param value:缓存的值
    :return:查到的数据
    '''
    conf = configobj.ConfigObj(cache_path,encoding="utf-8")
    sec_keys = conf.keys()
    if value == "":
        logger("写入没传递value","WARNING")

    #字典形式传参，
    elif opts == "" and isinstance(value,dict):
        logger("写入传参为字典", "info")
        if not sec_keys.count(sec):
            conf[sec] = {}
        for key,data in value.items():
            print(key,data)
            conf[sec][key] = data

    elif opts !="" and value !="":
        if not sec_keys.count(sec):
            conf[sec] = {}
        conf[sec][opts] = value

    else:
        logger("未知错误","WARNING")
    conf.write()
    return "缓存完成"


def read_conf_network_process(sec,config_path,data):
    main_url = read_conf(config_path=config_path, sec="CONFIG", opts="test_main_url")
    path_url = read_conf(config_path=config_path, sec=sec, opts="url")
    method = read_conf(config_path=config_path, sec=sec, opts="method")
    res = runmethod.network_process(url=main_url+path_url, method=method, data=data)
    return res

if __name__ == "__main__":
    write_cache()