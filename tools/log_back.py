import logging.handlers
import os
# filename = os.path.dirname(os.getcwd())+"\\"+"log\\tpshop.log"
filename = os.getcwd()+os.sep+"log"+os.sep+"tpshop.log"

log_level = {"debug": logging.DEBUG,
             "info": logging.INFO,
             "error": logging.ERROR,
             "warning": logging.WARNING,
             "critical":logging.CRITICAL}

class TestLog():
    def __init__(self, level):
        # 获取logger日志器
        self.logger = logging.getLogger()
        # 设置log级别
        self.logger.setLevel(logging.DEBUG)
        # 获取处理器 控制台
        # sf = logging.StreamHandler()
        # 获取处理器 文件已天为单位
        tf = logging.handlers.TimedRotatingFileHandler(filename,
                                                       when="midnight",
                                                       interval=1,
                                                       backupCount=10,
                                                       encoding="utf-8")
        tf.setLevel(log_level.get(level))
        # 定义格式器
        fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
        formatter = logging.Formatter(fmt)
        # 将格式器添加到处理器
        # sf.setFormatter(formatter)
        tf.setFormatter(formatter)
        # 将处理器添加到日志器
        # self.logger.addHandler(sf)

        self.logger.addHandler(tf)

    def get_log(self):
        return self.logger