from time import sleep

import time

import page
from selenium.webdriver.support.wait import WebDriverWait
from tools.log import TestLog

log = TestLog().get_log("info")


class Base:
    log.info("[Base]:开始执行")
    def __init__(self, driver):
        self.driver = driver
        log.info("[Base]:获取传递driver对象：{}".format(self.driver))

    # 获取元素 封装
    def base_find_element(self, loc, timeout=30, poll=1):
        log.info("[Base]查找元素操作：{}".format(loc))
        return WebDriverWait(self.driver, timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 点击元素 封装
    def base_click_element(self, loc):
        self.base_find_element(loc).click()
        log.info("[Base]点击操作：{}".format(loc))

    # 输入元素 封装
    def base_input_text(self, loc, value):
        el = self.base_find_element(loc)
        el.clear()
        log.info("[Base]清除文本操作：{}".format(loc))
        el.send_keys(value)
        log.info("[Base]输入文本操作：{}{}".format(loc, value))

    # 截屏 封装
    def base_get_screenshot(self):
        self.driver.get_screenshot_as_file("./screenshot/{}.html".format(time.strftime("%Y_%m_%d %H_%M_%S")))
        log.info("[Base]截图操作：{}".format("./screenshot/{}.html".format(time.strftime("%Y_%m_%d %H_%M_%S"))))

    # 获取文本 封装
    def base_get_text(self, loc):
        log.info("[Base]获取文本操作：{}".format(loc))
        return self.base_find_element(loc).text

    # 切换iframe
    def base_switch_frame(self, frame):
        self.driver.switch_to.frame(frame)
        log.info("[Base]切换iframe表单操作：{}".format(frame))

    # 回到默认目录
    def base_default_frame(self):
        self.driver.switch_to.default_content()
        log.info("[Base]切换iframe表单默认目录")
    # 刷新页面
    def base_refresh(self):
        sleep(3)
        self.driver.refresh()

    # 切换窗口
    def base_switch_to_window(self, title):
        self.driver.switch_to.window(self.base_get_handle(title))
        log.info("[Base]切换窗口表单操作：{}".format(title))

    # 根据title获取handle
    def base_get_handle(self, title):
        current = self.driver.current_window_handle
        log.info("[Base]获取当前窗口句柄：{}".format(title))
        handles = self.driver.window_handles
        log.info("[Base]获取当前所有窗口句柄：{}".format(handles))
        for handle in handles:
            log.info("[Base]开始遍历所有窗口句柄{}in：{}".format(handle, handles))
            self.driver.switch_to.window(handle)
            log.info("[Base]切换窗口句柄：{}".format(handle, handles))
            log.info("[Base]判断当前句柄窗口title{}是否为：{}".format(self.driver.title, title))
            if self.driver.title == title:
                log.info("[Base]判断当前句柄窗口title：{}等于：{}, 返回当前窗口句柄".format(self.driver.title, title))
                return handle
        return current

    # 查找元素方法 封装
    def base_find_element_exist(self, loc):
        try:
            if self.base_find_element(loc, timeout=3):
                log.info("[Base]查找{}元素存在！".format(loc))
                return True
        except:
            return False

    # 打开首页
    def base_get_index(self):
        self.driver.get(page.url)
        log.info("[Base]打开首页操作：{}".format(page.url))
