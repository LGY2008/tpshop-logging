import unittest
from time import sleep

from base.get_driver import GetDriver
from page.page_cart import PageCart
from page.page_login import PageLogin
from tools.log import TestLog

log = TestLog().get_log("info")


class TestCart(unittest.TestCase):
    log.info("[TestCart]:  购物车用例开始执行")
    def setUp(self):
        # 获取diver
        self.driver = GetDriver().get_driver()
        log.info("[TestCart]:  获取driver对象")
        # 获取PageCart对象
        self.cart = PageCart(self.driver)
        log.info("[TestCart]:  获取购物车对象")
        # 获取PageLogin对象
        self.login = PageLogin(self.driver)
        log.info("[TestCart]:  获取登录页面对象")
        # 点击登录连接
        self.login.page_click_login_link()
        log.info("[TestCart]:  点击登录连接")
        # 登录
        self.login.page_login_static()
        log.info("[TestCart]:  执行登录")
        sleep(3)
        # 回到首页
        self.cart.base_get_index()
        log.info("[TestCart]:  回到首页")
    def tearDown(self):
        # 关闭浏览器
        GetDriver().quit_driver()
        log.info("[TestCart]:  关闭driver对象")

    def test_add_cart(self, key="小米手机", expect_result="添加成功"):
        try:
            # 调用添加购物车方法
            self.cart.page_add_goods_cart(key)
            log.info("[TestCart]:  调用添加购物车操作方法")
            # 断言获取添加结果提示信息
            result = self.cart.page_get_add_cart_info()
            log.info("[TestCart]:  添加购物车后提示信息：{}".format(result))
            self.assertEqual(expect_result, result)
            # 回到默认页面
            self.cart.base_default_frame()
            log.info("[TestCart]:  回到iframe默认页面")
            # 关闭提示信息框
            self.cart.page_click_close_iframe()
            log.info("[TestCart]:  关闭提示添加成功后的信息框")
        except Exception as e:
            log.error(e)

if __name__ == '__main__':
    unittest.main()