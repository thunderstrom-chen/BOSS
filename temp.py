data = {
    "网址": "https://www.zhipin.com/?city=100010000&ka=city-sites-100010000",
    "登录按钮_XPATH": ("By.XPATH", '//*[@id="header"]/div[1]/div[4]/div/a[5]')
}


def aso(*value):
    a = value[0][0]
    b = value[0][1]
    print(a, "\n", b)


aso(data["登录按钮_XPATH"])
