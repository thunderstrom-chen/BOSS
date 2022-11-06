"""
demo文件的临时数据处理文件

"""
# import time
from selenium import webdriver
# from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

data = {
    "网址": "https://www.zhipin.com/?city=100010000&ka=city-sites-100010000",
    "登录按钮_XPATH": ("By.XPATH", '//*[@id="header"]/div[1]/div[4]/div/a[5]')
}

driver_path = "D:/python/driver/107.0.5304.18/chromedriver.exe"
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)


def aso():
    driver.get(data["网址"])


aso()
