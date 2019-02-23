import unittest
from time import sleep

from base.get_driver import GetDriver
from page.page_login import PageLogin
from page.page_pay import PagePay
from tools.log import TestLog
# 获取日志对象
log = TestLog().get_log("info")


class TestPay(unittest.TestCase):
    log.info("[TestPay]：支付模块用例")
    def setUp(self):
        # 获取dirver
        self.driver = GetDriver().get_driver()
        log.info("[TestPay]：获取driver对象：{}".format(self.driver))
        # 实例化 登录对象
        self.login = PageLogin(self.driver)
        log.info("[TestPay]：获取登录对象：{}".format(self.login))
        # 实例化 PagePay对象
        self.pay = PagePay(self.driver)
        log.info("[TestPay]：获取支付对象：{}".format(self.pay))
        # 点击 登录连接地址
        self.login.page_click_login_link()
        log.info("[TestPay]：点击登录地址：{}".format(self.driver.current_url))
        # 执行登录 操作
        self.login.page_login_static()
        log.info("[TestPay]：执行登录业务脚本成功")
        # 回到首页
        self.login.base_get_index()
        log.info("[TestPay]：回到首页地址：{}".format(self.driver.current_url))
    def tearDown(self):
        # 关闭driver
        GetDriver().quit_driver()
        log.info("[TestPay]：退出driver对象，driver：{}".format(self.driver))

    def test_pay(self):
        try:
            # 调用支付业务代码
            self.pay.page_pay()
            log.info("[TestPay]：调用支付业务成功")
            # 断言
            result = self.pay.page_get_payment_result()
            self.assertIn("订单提交成功", result)
            log.info("[TestPay]：断言支付状态成功，返回信息：{}".format(result))
        except Exception as e:
            log.error("支付业务出错，详情：{}".format(e))


if __name__ == '__main__':
    unittest.main()