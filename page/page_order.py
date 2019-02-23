import page
from base.base import Base


class PageOrder(Base):
    # 点击 购物车按钮
    def page_click_my_cart(self):
        self.base_click_element(page.my_cart_btn)

    # 点击 全选
    def page_click_all_select(self):
        el = self.base_find_element(page.my_cart_all_select)
        if not el.is_selected():
            el.click()

    # 点击 去结算按钮
    def page_click_account(self):
        self.base_click_element(page.my_cart_account_btn)

    # 定位收货人
    def page_click_consignee(self):
        self.base_find_element(page.my_cart_consignee, poll=0.5)

    # 点击 提交订单
    def page_click_submit(self):
        self.base_click_element(page.my_cart_submit_btn)

    # 获取 订单结果
    def page_get_submit_order_result(self):
        return self.base_get_text(page.my_cart_submit_result)

    # 组装订单业务
    def page_submit_order(self):
        self.page_click_my_cart()
        self.page_click_all_select()
        self.page_click_account()
        self.page_click_consignee()
        self.page_click_submit()
