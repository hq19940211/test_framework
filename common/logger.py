#!/usr/bin/python3
# Author:Maweiqing
# -*- coding: utf-8 -*-
# @Time     :2021/2/22 10:30
# @Software: PyCharm
import logging
import logging.handlers
import datetime
import os,sys

def logger(message,loglevel='info'):
    '''
    :param message: 记录log的数据
    :param loglevel: 日志的级别
    :return:
    '''
    file_path = "../logs/"
    file_name = str(datetime.date.today())

    #写入文件
    logger = logging.getLogger("interfaceframework_log")
    logger.setLevel(logging.DEBUG)
    rf_handler = logging.handlers.TimedRotatingFileHandler(file_path+file_name+".log",when='midnight',interval=7,atTime=datetime.time(0, 0, 0, 0,),backupCount=15,encoding='utf-8')
    rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

    #控制台展示
    ch_handler = logging.StreamHandler()
    ch_handler.setLevel(logging.DEBUG)

    logger.addHandler(rf_handler)
    logger.addHandler(ch_handler)

    if loglevel.upper() in "DEBUG":
        logger.debug(message)

    elif loglevel.upper() in "INFO":
        logger.info(message)

    elif loglevel.upper() in "WARNING":
        logger.warning(message)

    elif loglevel.upper() in "ERROR":
        logger.error(message)

    elif loglevel.upper() in "CRITICAL":
        logger.critical(message)

    else:
        logger.error("日志level错误")


if __name__ == '__main__':
    logger(message="错误133331111",loglevel="WARNING")