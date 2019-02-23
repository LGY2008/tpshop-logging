from time import sleep

import page
from base.base import Base


class PageCart(Base):
    # 首页搜索框内输入 关键词
    def page_input_search_key(self, key):
        self.base_input_text(page.cart_search_input, key)

    # 点击搜索按钮
    def page_click_search_btn(self):
        self.base_click_element(page.cart_search_btn)

    # 点击搜索到的商品
    def page_click_goods(self):
        self.base_click_element(page.cart_add_cart_info)

    # 在商品详情页点击添加到购物车
    def page_click_goods_cart(self):
        self.base_click_element(page.cart_join_cart)

    # 获取添加购物车结果提示信息
    def page_get_add_cart_info(self):
        sleep(2)
        el = self.base_find_element(page.cart_iframe_element)
        # 切换iframe表单
        self.base_switch_frame(el)
        return self.base_get_text(page.cart_add_cart_result)

    def page_click_close_iframe(self):
        self.base_click_element(page.cart_close_iframe)

    # 组装添加购物车 业务流程
    def page_add_goods_cart(self, key):
        self.page_input_search_key(key)
        self.page_click_search_btn()
        self.page_click_goods()
        self.page_click_goods_cart()
