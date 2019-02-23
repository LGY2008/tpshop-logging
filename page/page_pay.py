from time import sleep

import page
from base.base import Base


class PagePay(Base):
    # 点击 我的订单
    def page_click_my_order(self):
        self.base_click_element(page.pay_my_order_link)

    # 点击 待付款
    def page_click_obligation(self):
        # 切换窗口
        self.base_switch_to_window(page.pay_my_order_title)
        self.base_click_element(page.pay_obligation)

    # 点击 立即支付
    def page_click_payment(self):
        self.base_click_element(page.pay_payment)

    # 选择 货到付款
    def page_click_cargo_pay(self):
        # 切换窗口
        self.base_switch_to_window(page.pay_payment_title)
        self.base_click_element(page.pay_cargo_pay)

    # 确认 支付方式
    def page_confirm_payment(self):
        self.base_click_element(page.pay_confirm_payment)

    # 获取 支付结果
    def page_get_payment_result(self):
        return self.base_get_text(page.pay_result)

    # 支付业务方法 封装
    def page_pay(self):
        self.page_click_my_order()
        self.page_click_obligation()
        self.page_click_payment()
        self.page_click_cargo_pay()
        sleep(2)
        self.page_confirm_payment()
