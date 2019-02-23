import unittest

import time

from tools.HTMLTestRunner import HTMLTestRunner

# 定义测试套件
suite = unittest.defaultTestLoader.discover("./scripts", pattern="test*.py")
# 运行测试套件 并 生成测试用例
with open("./report/{}.html".format(time.strftime("%Y_%m_%d %H_%M_%S")), "wb") as f:
    HTMLTestRunner(stream=f).run(suite)

