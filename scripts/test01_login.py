import unittest

from base.get_driver import GetDriver
from page.page_login import PageLogin
from parameterized import parameterized
from tools.log import TestLog
from tools.read_yaml import ReadYaml

# 获取日志器
log = TestLog().get_log("info")


# 读取测试数据
def get_data():
    arrs = []
    for data in ReadYaml("login.yaml").read_yaml().values():
        arrs.append((data.get("username"),
                     data.get("password"),
                     data.get("verify_code"),
                     data.get("expect_info"),
                     data.get("expect_msg")))
    return arrs


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        try:
            # 实例化 driver
            cls.driver = GetDriver().get_driver()
            log.info("[TestLogin]: 实例化driver")

            # 实例化 PageLogin
            cls.login = PageLogin(cls.driver)
            log.info("[TestLogin]: 实例化PageLogin对象")

            # 打开登录连接
            cls.login.page_click_login_link()
            log.info("[TestLogin]: 初次打开登录连接地址")
        except Exception as e:
            log.error(e)

    @classmethod
    def tearDownClass(cls):
        GetDriver().quit_driver()
        log.info("[TestLogin]: 退出driver驱动对象")

    @parameterized.expand(get_data())
    def test_login(self, username, pwd, verify_code, expect_info, expect_msg):
        login = self.login
        # 判断是否正向用例
        log.info("[TestLogin]: 判断是否为[正向]用例：{}".format(expect_info == "1380"))

        if expect_info:
            try:
                # 调用登录方法
                login.page_login(username, pwd, verify_code)
                log.info("[TestLogin]: 调用登录方法，username:{},pwd:{},verify_code:{}".format(username, pwd, verify_code))
                # 断言是否登录成功
                self.assertIn(expect_info, login.page_get_login_info())
                log.info("[TestLogin]: 登录成功")

                # 退出登录
                login.page_click_logout()
                log.info("[TestLogin]: 退出登录")

                # 断言是否退出成功
                self.assertTrue(login.page_is_logout())
                log.info("[TestLogin]: 退出登录成功")

                # 点击登录连接
                login.page_click_login_link()
                log.info("[TestLogin]: 退出登录后，点击登录连接")
            except Exception as e:
                log.error(e)
        else:
            try:
                # 判断是否正向用例
                log.info("[TestLogin]: 判断是否为[逆向]用例：{}".format(expect_info is None))

                login.page_login(username, pwd, verify_code)
                log.info("[TestLogin]: 调用登录方法，username:{},pwd:{},verify_code:{}".format(username, pwd, verify_code))

                # 断言异常提示信息
                self.assertIn(expect_msg, login.page_get_error_info())
                log.info("[TestLogin]: 调用登录方法，username:{},pwd:{},verify_code:{}->断言成功！".format(username, pwd, verify_code))

                # 点击确定
                login.page_click_confirm_btn()
                log.info("[TestLogin]: 点击确定")
            except Exception as e:
                log.error(e)


if __name__ == '__main__':
    unittest.main()
