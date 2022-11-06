import json

file = open("BOSS.json", "r", encoding="utf-8")
file_data = json.load(file)
print(file_data['输入手机号文本框'])
