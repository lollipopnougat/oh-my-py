#爬中国天气网数据 UTF-8
#18.2.12 更新 chrome 用户代理字符
#18.3.4 更新2.0 新增读取json查询其他城市
import requests
import re
import json
import os


def request_and_re(url, header):

    os.system("cls")
    try:
        r = requests.get(url, headers=header)
        print(r.status_code)
        #返回请求状态码
        r.encoding = r.apparent_encoding
        p1 = r"\"7d\":\[\[\".+\]\]}"
        pattern1 = re.compile(p1)
        #编译成正则表达式
        list0 = pattern1.findall(r.text)
        #搜寻全部符合条件的字符串,返回结果队列
        resul = list0[0]
        #print(resul[8:-6]) #测试用
        p2 = r"[d|n]0\d,|,\d\",\"|,\d\"\],\[\"|\"7d\":\[\[\"|[d|n]1\d,"
        pattern2 = re.compile(p2)
        list1 = pattern2.split(resul[8:-6])
        #对结果进行修饰
        dis1 = list1[0]
        print("下面是7天天气预报：\n")
        for x in range(len(list1)):
            print(list1[x])
            if (x % 2 != 0):
                print("\n")
                #整齐输出
    except:
        print("有点问题了....")
    input()


def chose_city():
    print("A:直辖市\nB:省/自治区\n")
    c = input("请选择(输入一个大写字母):")
    if c == 'A':
        print("A:北京\nB:上海\nC:天津\nD:重庆\n")
        d = input("请选择:")
        if d == 'A':
            return cit["BJ"]
        elif d == 'B':
            return cit["SH"]
        elif d == 'C':
            return cit["TJ"]
        elif d == 'D':
            return cit["CQ"]
        else:
            print("输入有误哦\n")
    elif c == 'B':
        print("A:山东\nB:陕西\nC:云南\nD:安徽\nE:江西\nF:吉林\nG:新疆")
        d = input("请选择:")
        if d == 'A':
            print("A:济南\nB:青岛\nC:枣庄\nD:邹平\n")
            e = input("请选择:")
            if e == 'A':
                return cit["SD"]["JN"]
            elif e == 'B':
                return cit["SD"]["QD"]
            elif e == 'C':
                return cit["SD"]["ZZ"]
            elif e == 'D':
                return cit["SD"]["ZP"]
            else:
                print("输入有误哦\n")

        elif d == 'B':
            print("A:西安\nB:榆林\nC:汉中\n")
            e = input("请选择:")
            if e == 'A':
                return cit["SX"]["XA"]
            elif e == 'B':
                return cit["SX"]["YL"]
            elif e == 'C':
                return cit["SX"]["HZ"]
            else:
                print("输入有误哦\n")
        elif d == 'C':
            print("A:昆明\nB:玉溪\n")
            e = input("请选择:")
            if e == 'A':
                return cit["YN"]["KM"]
            elif e == 'B':
                return cit["YN"]["YX"]
            else:
                print("输入有误哦\n")
        elif d == 'D':
            print("A:合肥\nB:池州\n")
            e = input("请选择:")
            if e == 'A':
                return cit["AH"]["HF"]
            elif e == 'B':
                return cit["AH"]["CZ"]
            else:
                print("输入有误哦\n")
        elif d == 'E':
            print("A:南昌\nB:赣州\n")
            e = input("请选择:")
            if e == 'A':
                return cit["JX"]["NC"]
            elif e == 'B':
                return cit["JX"]["GZ"]
            else:
                print("输入有误哦\n")
        elif d == 'F':
            print("A:长春\nB:吉林\n")
            e = input("请选择:")
            if e == 'A':
                return cit["JL"]["CC"]
            elif e == 'B':
                return cit["JL"]["JL"]
            else:
                print("输入有误哦\n")
        elif d == 'G':
            print("A:乌鲁木齐\nB:沙湾\n")
            e = input("请选择:")
            if e == 'A':
                return cit["XJ"]["WLMQ"]
            elif e == 'B':
                return cit["XJ"]["SW"]
            else:
                print("输入有误哦\n")
        else:
            print("输入有误哦\n")
    else:
        print("输入有误哦\n")
    input()


f = open("weatherconfig.json", encoding='utf-8')
cit = json.load(f)
#从json文件中读取数据

print("天气爬虫\n版本Ver 2.0 Beta2\n封掣·2018\n黑科技开发小组")

chosen = chose_city()
url1 = "http://www.weather.com.cn/weather/" + str(chosen) + ".shtml"
#整合的地址
header1 = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
}
#chrome浏览器（Windows10 64bit）的用户标识
request_and_re(url1, header1)
