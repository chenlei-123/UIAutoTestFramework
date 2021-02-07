from appium.webdriver.common.mobileby import MobileBy

from page.base_page import BasePage


class Main(BasePage):
    def goto_search(self):
        # self.find(MobileBy.ID, "com.xueqiu.android:id/home_search").click()
        self.steps("../page/main.yaml")

    def goto_windows(self):
        # 点击，弹出登录弹窗干扰
        self.find(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']").click()
        # 自动点击black_list中的元素
        # 再点击搜索
        self.find(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/home_search']").click()
