import unittest
from time import sleep

from base.get_driver import GetDriver
from page.page_login import PageLogin
from page.page_order import PageOrder
from tools.log import TestLog

log = TestLog().get_log("info")


class TestOrder(unittest.TestCase):
    log.info("[TestOrder]:订单模块测试用例")
    def setUp(self):
        try:
            # 获取driver对象
            self.driver = GetDriver().get_driver()
            log.info("[TestOrder]: 获取driver对象")
            # 获取登录对象
            self.login = PageLogin(self.driver)
            log.info("[TestOrder]: 获取登录对象")
            # 点击登录连接
            self.login.page_click_login_link()
            log.info("[TestOrder]: 点击登录连接")
            # 登录
            self.login.page_login_static()
            log.info("[TestOrder]: 执行登录成功")
            # 回到首页
            self.login.base_get_index()
            log.info("[TestOrder]: 回到首页")
            # 获取 PageOrder对象
            self.order = PageOrder(self.driver)
            log.info("[TestOrder]: 获取PageOrder对象")
        except Exception as e:
            log.error(e)
    def tearDown(self):
        # 关闭drive对象
        GetDriver().quit_driver()
        log.info("[TestOrder]: 关闭driver对象")

    def test_order(self):
        try:
            # 调用提交订单方法
            order = self.order
            order.page_submit_order()
            log.info("[TestOrder]: 执行提交订单业务")
            result = order.page_get_submit_order_result()
            self.assertIn("订单提交成功", result)
            log.info("[TestOrder]: 订单断言成功，断言信息：{}".format(result))
        except Exception as e:
            log.error(e)


if __name__ == '__main__':
    unittest.main()