import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# 所有数据
data = {
    "网址": "https://www.zhipin.com/?city=100010000&ka=city-sites-100010000",
    "登录按钮_XPATH": '//*[@id="header"]/div[1]/div[4]/div/a[5]',
    "职位": "软件测试",
    "搜索职位输入框_class_name": "ipt-search",
    "搜索按钮_XPATH": '//*[@id="wrap"]/div[3]/div/div[1]/div[1]/form/button',
    "立即沟通_class": "btn btn-startchat"
}


class Boss:
    def __init__(self):
        # 设置驱动
        driver_path = "D:/python/driver/107.0.5304.18/chromedriver.exe"
        service = Service(executable_path=driver_path)
        self.driver = webdriver.Chrome(service=service)
        # 错误列表 接收的参数包含：时间，错误指向，错误类型，具体错误，
        self.er_list = []


class boss_ele(Boss):
    @staticmethod
    def time_str():
        return time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))  # 获取时间

    def driver_ele(self, value):
        """
        进行元素element获取
        :param value:
        :return:
        """
        try:
            return self.driver.find_element(By.ID, value)
        except BaseException as b:
            self.er_list.append(
                str(self.time_str()) + "元素获取错误" + str(b) + "输入元素为：" + str(value) + "元素定位方式为ID")
            try:
                return self.driver.find_element(By.XPATH, value)
            except BaseException as b:
                self.er_list.append(
                    str(self.time_str()) + "元素获取错误" + str(b) + "输入元素为：" + str(value) + "元素定位方式为XPATH")
                try:
                    return self.driver.find_element(By.CLASS_NAME, value)
                except BaseException as b:
                    self.er_list.append(str(self.time_str()) + "元素获取错误" + str(b) + "输入元素为：" + str(value) +
                                        "元素定位方式为CLASS_NAME")
                    try:
                        return self.driver.find_element(By.NAME, value)
                    except BaseException as b:
                        self.er_list.append(str(self.time_str()) + "元素获取错误" + str(b) + "输入元素为：" + str(
                            value) + "元素定位方式为NAME")
                        try:
                            return self.driver.find_element(By.TAG_NAME, value)
                        except BaseException as b:
                            self.er_list.append(str(self.time_str()) + "元素获取错误" + str(b) + "输入元素为：" + str(
                                value) + "元素定位方式为TAG_NAME")
                            try:
                                return self.driver.find_element(By.CSS_SELECTOR, value)
                            except BaseException as b:
                                self.er_list.append(str(self.time_str()) + "元素获取错误" + str(b) + "输入元素为：" +
                                                    str(value) + "元素定位方式为CSS_SELECTOR")

    def driver_click(self, *value):
        """
        进行点击操作
        :param value:
        :return:
        """
        try:
            element = self.driver_ele(value)
            element.click()
        except BaseException as b:
            self.er_list.append(str(self.time_str()) + "元素进行点击" + str(b) + "输入元素为：" + str(
                value) + "元素定位方式为CSS_SELECTOR")

    def driver_send_key(self, text, *value):
        """
        进行文本输入操作
        :param text:
        :param value:
        :return:
        """
        element = self.driver_ele(*value)
        element.send_keys(text)

    def driver_hande(self):
        """
        进行页面的切换
        获取页面句柄
        :return:
        """
        self.driver.switch_to.window(self.driver.window_handles[-1])


class login(boss_ele):
    """
    进行登录操作
    """

    def url_get(self):
        """
        进行网址访问，并将网页最大化
        :return:
        """
        self.driver.get(data["网址"])
        self.driver.maximize_window()

    def login(self):
        """
        进行登录
        :return:
        """
        self.driver_click(data["登录按钮_XPATH"])  # 点击登录按钮
        self.driver_hande()  # 获取页面的句柄
        time.sleep(10)  # 等待10秒进行登录
        self.driver_hande()  # 重新获取页面句柄

    def search_job(self):
        """
        进行搜索
        :return:
        """
        self.driver_send_key(data["职位"], data["搜索职位输入框_class_name"])  # 进行岗位输入
        self.driver_click(data["搜索按钮_XPATH"])  # 点击搜索按钮

    # 进行沟通  进行沟通时列表，需要进行循环点击
    def link_up(self):
        self.driver_ele(data["立即沟通_class"]).click()


class runner(login):
    """
    进行文件的执行
    """

    def run_main(self):
        self.url_get()  # 访问网址
        time.sleep(10)
        # self.login()  # 进行登录
        self.search_job()  # 搜索工作
        time.sleep(5)

    # 输出错误列表
    def er_print(self):
        # 打印错误列表
        for i in self.er_list:
            print(i)


if __name__ == '__main__':
    runner().run_main()
    runner().er_print()
