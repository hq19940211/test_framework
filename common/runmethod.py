#!/usr/bin/python3
# Author:Maweiqing
# -*- coding: utf-8 -*-
# @Time     :2021/2/22 15:26
# @Software: PyCharm
import requests,configparser
import json,hashlib
import pymysql
import urllib
import random
import string
from common import logger
# from crypto import Random



def network_process(url, method, data=None, params=None, headers=None, cookies=None, files=None, timeout=None):
    # 通用网络请求组件
    '''

    :param url: 地址
    :param method: 接口模式
    :param data: 数据
    :param params: get数据
    :param headers: 头数据
    :param cookies: 缓存数据
    :param files: 文件
    :param timeout: 超时
    :return:
    '''
    method = method.upper()

    try:
        logger.logger(message="请求数据:"+data)
        res = requests.request(method, url, data=data,params=params, headers=headers, cookies=cookies, files=files,
                               timeout=timeout,verify=False)
        logger.logger(message="返回数据:"+res.content.decode("utf-8"))

        time = res.elapsed.total_seconds()
        if res.status_code == requests.codes.ok:
            resp = json.loads(res.content)
            if 0 == resp['code']:
                return {'status': True, 'data': resp, 'time': time, 'message': 'success',"cookies":res.cookies}
            else:
                return {'status': False, 'message': resp['message']}
        else:
            return {'status': False, 'message': 'requests code {0}'.format(res.status_code)}
    except Exception as e:
        logger.logger(message="请求失败:"+str(e))
        return {'status': False, 'message': str(e)}



def mysql_process(host=None, port=None, user=None, password=None, db=None, sql=None):
    # 返回一条SQL查询结果
    '''
    :param host: 地址
    :param port: 接口
    :param user: 用户名
    :param password: 密码
    :param db: 库名
    :param sql: sql语句
    :return:
    '''
    try:
        conn = pymysql.connect(host=host, port=port, user=user, password=password, db=db)
        cursor = conn.cursor()
        cursor.execute(sql)
        results = cursor.fetchone()
        cursor.close()
        conn.close()
        return results
    except Exception as e:
        print (e)

def mysql_process_all(host=None, port=None, user=None, password=None, db=None, sql=None):
    # 返回所有SQL查询结果
    try:
        conn = pymysql.connect(host=host, port=port, user=user, password=password, db=db)
        cursor = conn.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return results
    except Exception as e:
        print (e)


def mysql_process_change(host=None, port=None, user=None, password=None, db=None, sql=None):
    # 执行增删改操作
    try:
        conn = pymysql.connect(host=host, port=port, user=user, password=password, db=db)
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(e)


def compare_process(dicts, DB, deleteKey=None):
    # API请求值和DB值比较,deleteKey->list
    # print(DB)
    # print(dicts)
    try:
        data = dicts
        status = True
        msg = ''
        if deleteKey is not None:  # 删除不需要比对的key
            for a in range(len(deleteKey)):
                data.pop(deleteKey[a])
        values = data.values()
        values = sorted(values)
        DB =sorted(DB)
        for i in range(len(values)):
            if values[i] != DB[i]:
                status = False
                msg += u'预期值不相等,期望值-->{0},DB值-->{1}\n'.format(values[i], DB[i])
        return {'status': status, 'message': msg}
    except Exception as e:
        print (e)





def md5(sign):
    md = hashlib.md5()
    md.update(sign.encode("utf-8"))
    sign = md.hexdigest()
    return sign


def write_cache(opts,value,cache_path,sec="CACHE"):
    conf =configparser.ConfigParser()
    if not conf.has_section(sec):
        conf.add_section(sec)
    conf.read(cache_path, encoding="utf-8")
    conf.set(sec,opts,value)
    with open(cache_path,'w',encoding="utf-8") as f:
        conf.write(f)







# if __name__ == "__main__":
#     read_conf(sec = "MAIN",opts = "main_url",config_path="config.ini")