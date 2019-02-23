import page
from base.base import Base


class PageLogin(Base):

    # 点击登录连接
    def page_click_login_link(self):
        self.base_click_element(page.login_link)


    # 输入用户名
    def page_input_username(self, username):
        self.base_input_text(page.login_username, username)

    # 输入密码
    def page_input_pwd(self, pwd):
        self.base_input_text(page.login_pwd, pwd)

    # 输入验证码
    def page_input_verify_code(self, verify_code):
        self.base_input_text(page.login_verify_code, verify_code)

    # 点击登录
    def page_click_login_btn(self):
        self.base_click_element(page.login_btn)

    # 获取登录后信息
    def page_get_login_info(self):
        return self.base_get_text(page.login_info)

    # 退出登录
    def page_click_logout(self):
        self.base_click_element(page.login_logout)

    # 判断是否退出成功
    def page_is_logout(self):
        return self.base_find_element_exist(page.login_link)

    # 登录方法封装
    def page_login(self, username, pwd, verify_code):
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_input_verify_code(verify_code)
        self.page_click_login_btn()

    # 正向用例 登录依赖
    def page_login_static(self, username="13800001111", pwd="123456", verify_code="8888"):
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_input_verify_code(verify_code)
        self.page_click_login_btn()
        self.page_get_login_info()

    # 异常点击确定
    def page_click_confirm_btn(self):
        self.base_click_element(page.login_confirm)

    # 获取异常提示信息
    def page_get_error_info(self):
        return self.base_get_text(page.login_error_info)