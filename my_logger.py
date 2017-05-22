#!/usr/bin/python
# -*- coding: utf-8 -*-  
import logging

def get_logger():
    logger = logging.getLogger()  
    logger.setLevel(logging.INFO)  #设置日志输出的总开关，只有超过INFO级别的日志会输出。
  
    logfile = './log.txt'  
    lf = logging.FileHandler(logfile, mode='a+')  #创建文件Handler对象
    lf.setLevel(logging.DEBUG)   #
  

    ld = logging.StreamHandler()      #创建控制台StreamHandler对象
    ld.setLevel(logging.INFO) #
  

    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")  
    lf.setFormatter(formatter)  #设置format
    ld.setFormatter(formatter)  
  

    logger.addHandler(lf)  
    logger.addHandler(ld)  #添加输出handle对象

    return logger

if __name__ == "__main__":
    logger = get_logger()
    logger.debug('debug log')
    logger.info('info log')
    logger.warning('warning log')
    logger.error('error log')
    logger.critical('critical log')
