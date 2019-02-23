from selenium.webdriver.common.by import By

url = "http://127.0.0.1"

"""登录数据"""
# 登录连接文本
login_link = By.LINK_TEXT, "登录"
# 用户名
login_username = By.ID, "username"
# 密码
login_pwd = By.ID, "password"
# 验证码
login_verify_code = By.ID, "verify_code"
# 登录按钮
login_btn = By.NAME, "sbtbutton"
# 登录后信息
login_info = By.CLASS_NAME, "userinfo"
# 退出登录
login_logout = By.LINK_TEXT, "安全退出"
# 异常窗口 点击确定按钮
login_confirm = By.XPATH, "//*[text()='确定']"
# 异常提示信息
login_error_info = By.CLASS_NAME, "layui-layer-padding"

"""购物车配置数据"""
# 搜索商品文本框
cart_search_input = By.CSS_SELECTOR, "#q"
# 搜索按钮
cart_search_btn = By.CSS_SELECTOR, ".ecsc-search-button"
# 点击加入购物车->跳转到商品详情页面
cart_add_cart_info = By.CSS_SELECTOR, ".p-btn>a"
# 添加到购物车
cart_join_cart = By.CSS_SELECTOR, "#join_cart"
# 获取添加到购物车后提示信息 是否添加成功 需要切换iframe标签
cart_add_cart_result = By.CSS_SELECTOR, ".conect-title>span"
# 切换iframe 通过元素标签切换
cart_iframe_element = By.CSS_SELECTOR, "iframe"
# 通过name切换
cart_iframe_name = "layui-layer-iframe1"
# 关闭iframe提示信息框
cart_close_iframe = By.CSS_SELECTOR, ".layui-layer-ico"

"""我的购物车信息"""
# 我的购物车 按钮
my_cart_btn = By.CSS_SELECTOR, ".c-n.fl"
# 点击全选复选框
my_cart_all_select = By.CSS_SELECTOR, ".checkCartAll"
# 点击 去结算
my_cart_account_btn = By.CSS_SELECTOR, ".gwc-qjs"
# 定位 收货人
my_cart_consignee = By.CSS_SELECTOR, ".address_id>input"
# 提交订单 按钮
my_cart_submit_btn = By.CSS_SELECTOR, ".gwc-qjs>span"
# 获取文本结果
my_cart_submit_result = By.CSS_SELECTOR, ".erhuh>h3"

"""支付页面"""
# 我的订单 连接
pay_my_order_link = By.LINK_TEXT, "我的订单"
# 待付款
pay_obligation = By.LINK_TEXT, "待付款"
# 立即支付
pay_payment = By.LINK_TEXT, "立即支付"
# 货到付款
pay_cargo_pay = By.CSS_SELECTOR, "[src='/plugins/payment/cod/logo.jpg']"
# 确认支付方式
pay_confirm_payment = By.CSS_SELECTOR, ".button-confirm-payment"
# 支付结果
pay_result = By.CSS_SELECTOR, ".erhuh>h3"
# 窗口 我的订单 title [选择待付款之前要切换窗口]
pay_my_order_title = "我的订单"
# 窗口 立即支付 title [选择货到付款之前要切换窗口]
pay_payment_title = "订单支付-开源商城 | B2C商城 | B2B2C商城 | 三级分销 | 免费商城 | 多用户商城 | tpshop｜thinkphp shop｜TPshop 免费开源系统 | 微商城"