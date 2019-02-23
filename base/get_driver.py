from time import sleep

from selenium import webdriver
import page


class GetDriver:
    __driver = None
    @classmethod
    def get_driver(cls):
        if cls.__driver is None:
            # cls.__driver = webdriver.Chrome()
            cls.__driver = webdriver.Firefox()
            cls.__driver.maximize_window()
            cls.__driver.implicitly_wait(30)
            cls.__driver.get(page.url)
        return cls.__driver

    @classmethod
    def quit_driver(cls):
        if cls.__driver:
            cls.__driver.quit()
            cls.__driver = None

if __name__ == '__main__':
    GetDriver().get_driver()
    GetDriver().quit_driver()