from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome


class postJsText:
    def __init__(self, url):
        self.url = url

    def getText(self):
        driver = webdriver.Chrome()
        driver.get(self.url)


text = postJsText("https://www.youtube.com")