# coding=utf-8
import logging

class Logger():
    def __init__(self,logName):
        logging.basicConfig(filename=logName + '.log',
                            format='[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]', level=logging.DEBUG,
                            filemode='w', datefmt='%Y-%m-%d %I:%M:%S %p')
        # # create logger
        # self.logger = logging.getLogger(logger)
        # self.logger.setLevel(logging.DEBUG)
        #
        # # 创建一个handler，用于写入日志文件
        # fh = logging.FileHandler(logName)
        # fh.setLevel(logLevel)

        # create control handler
        control = logging.StreamHandler()
        control.setLevel(logging.INFO)

        # 定义handler的输出格式
        log_format = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
#        fh.setFormatter(log_format)
        control.setFormatter(log_format)

        # 给logger添加handler
        logging.getLogger('').addHandler(control)

    def printlog(self,message):
        logging.info(message)