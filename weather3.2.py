# 爬中国天气网数据 UTF-8
# 18.2.12 更新 chrome 用户代理字符
# 18.3.4 更新2.0 新增读取json查询其他城市
# 18.5.13 更新3.0 新增其他几个城市
# 18.8.17 更新3.1 支持全国2586个城市 查询方式改变
# 19.1.21 更新3.2 全局变量的使用 结果显示城市名 更新chrome user-agent
# 19.4.22 更新3.2.1 ua更新
import requests
import re
import json
import os
"""
1e 3a 3e 4b 4e 5b 8f 9e
"""
city = ""

def RequestsAndReturn(url, header):
    global city
    os.system("cls")
    os.system("color 8a")
    try:
        r = requests.get(url, headers=header)
        print(r.status_code) # 返回请求状态码
        r.encoding = r.apparent_encoding
        p1 = r"\"7d\":\[\[\".+\]\]}"
        pattern1 = re.compile(p1) # 编译成正则表达式
        list0 = pattern1.findall(r.text) # 搜寻全部符合条件的字符串,返回结果队列
        resul = list0[0]
        # print(resul[8:-6]) #测试用
        p2 = r"[d|n]\d\d,|,\d\",\"|,\d\"\],\[\"|\"7d\":\[\[\""
        pattern2 = re.compile(p2)
        list1 = pattern2.split(resul[8:-6]) # 对结果进行修饰
        #dis1 = list1[0]
        print("下面是 " + city + " 7天天气预报：\n")
        for x in range(len(list1)):
            print(list1[x])
            if x % 2 != 0:
                print("\n") # 整齐输出
    except:
        os.system("color 4b")
        print("连接有点问题了....")
    os.system("pause")


def ChoseCity():
    global city
    try:
        c = input("请输入直辖市/省/自治区名称(格式：北京、宁夏、新疆):")
        if c == "澳门":
            city = c
            return cit[c]
        else:
            x = input("请输入市/区/县/旗名称(格式：海淀、丽江、呼和浩特、新竹):")
            city = x
            return cit[c][x]
    except:
        os.system("color 4b")
        print("\n\n请检查您的输入\n\n可能中国天气网上您的城市名与您输入的不同")
        print("\n一般是与天气网上您的地名没有‘省’、‘县’、‘市’字有关")
        input("\n按任意键继续")
        os.system("color 2e")
        return ChoseCity()


f = open("WeatherConfig3-1.json", encoding = "utf-8")
cit = json.load(f) # 从json文件中读取数据
# os.system("mode con cols=65 lines=40")
print("天气爬虫\n版本Ver 3.2 Beta1\n\nFC·Copyright\n封掣·2019\n\n")
os.system("color 9e")
chosen = ChoseCity()
url1 = "http://www.weather.com.cn/weather/" + str(chosen) + ".shtml" # 整合的地址
header1 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
} # chrome浏览器（Windows10 64bit）的用户标识
RequestsAndReturn(url1, header1)
