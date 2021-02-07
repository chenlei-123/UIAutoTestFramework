import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    _driver: WebDriver
    _black_list = [(MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/iv_close"]')]

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, locator, value):
        try:
            element = self._driver.find_element(locator, value)
            return element
        except:
            for black in self._black_list:
                elements = self._driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    break
            return self.find(locator, value)

    def click(self, locator, value):
        self.find(locator, value).click()

    def steps(self, path):
        with open(path) as f:
            steps = yaml.safe_load(f)
        print(steps)
        element = None
        for step in steps:
            if 'by' in step.keys():
                element = self.find(step['by'], step['locator'])
            if 'action' in step.keys():
                action = step['action']
                if action == 'click':
                    element.click()
