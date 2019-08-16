# -*- coding=utf-8 -*-
import os
import logging
import random
from itertools import islice
import win32con
import win32clipboard as w
import chardet
import logging

# 社会主义核心价值观.py ---  any text 2 core value
''' 
-------------------------------

请先安装依赖 pywin32 
顺便请确认chardet有没有安装

管理员身份进入powershell 
键入 "pip install pywin32 chardet" 
(当然前提是你得安好pip并配置好环境变量)

注意！ 本脚本在python 3.7.1 版本下良好运行， 低于此版本的尚未进行测试
参考了LNP于 2019.2.5编写的 b64.py

LNP 2019.4.22

好像Windows 10 1809以后记事本默认中文保存格式变成了utf-8,
于是就支持了一下，现在除了utf-8和GBK以外还支持了好几种编码格式(chardet支持)

LNP 2019.8.15
-------------------------------
'''


# win32con 即win api常量的python实现，C/C++一般都是在windows.h内大写的宏定义
# 采用pywin32调起系统剪贴板api
def GetText():
    w.OpenClipboard()
    d = w.GetClipboardData(win32con.CF_UNICODETEXT)
    w.CloseClipboard()
    return d


def SetText(aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
    w.CloseClipboard()


logging.basicConfig(level=logging.DEBUG)
VALUES = '富强民主文明和谐自由平等公正法治爱国敬业诚信友善'
VALUE_PAIR = ('富强', '民主', '文明', '和谐', '自由', '平等', "公正", '法治', "爱国", '敬业', '诚信',
              '友善')


def str2utf8(Str):
    for i in Str:
        for j in i.encode('utf-8').hex().upper():
            yield j


def hex2duo(Str):
    for h in str2utf8(Str):
        numH = int(h, 16)
        if numH < 10:
            yield (numH)
        elif random.random() < 0.5:
            yield (10)
            yield (numH - 10)
        else:
            yield (11)
            yield (numH - 6)


def duo2values(Str):
    for i in hex2duo(Str):
        yield VALUES[2 * i] + VALUES[2 * i + 1]


def EncodeCore():
    flag = True
    cur_encoding = ''
    while flag:
        inp = input("从文本文件(F)\n我自己输入/粘贴到控制台(P)\n读取剪贴板(R)\n直接退出(E)\n")
        if inp == "F" or inp == "f":
            FiName = input("请输入文件名(*.txt):")
            with open(FiName, 'rb') as f:
                cur_encoding = chardet.detect(f.read())['encoding']
                if cur_encoding == 'GB2312':
                    cur_encoding = 'GBK'
            Tfile = open(FiName, 'r', encoding=cur_encoding)
            tst = Tfile.read()
            Tfile.close()
            flag = False
        elif inp == "P" or inp == "p":
            tst = input("请输入源字符串:\n")
            flag = False
        elif inp == "R" or inp == "r":
            tst = GetText()
            flag = False
        elif inp == "E" or inp == "e":
            exit(0)
        else:
            print("输入有误！请重新选择:")
    txtfi = "".join(duo2values(tst))
    outo = input("输出到文本文件(F)\n拷贝到控制台(C)\n直接打印(P)\n退出(E)\n")
    if outo == "F" or outo == "f":
        OutName = input("请键入输出文件名(*.*):")
        Pfile = open(OutName, "w", encoding=cur_encoding)
        Pfile.write(txtfi)
        Pfile.close()
        print("输出完成，请打开同目录下 " + OutName + " 文件查看")
    elif outo == "P" or outo == "p":
        print(txtfi)
    elif outo == "C" or outo == "c":
        SetText(txtfi)
    elif outo == "E" or outo == "e":
        exit(0)
    else:
        print("输入有误！")


def values2duo(value):
    it = iter(value)
    for v in it:
        spicemen = v + next(it)
        if spicemen in VALUE_PAIR:
            yield VALUE_PAIR.index(spicemen)


def duo2hex(value):
    it = iter(values2duo(value))
    for v in it:
        if v < 10:
            yield v
        elif v == 10:
            yield 10 + next(it)
        else:
            yield 6 + next(it)


def valueDecode(value):
    it = iter(duo2hex(value))
    for v in it:
        ca = (v << 4) + next(it)
        if ca < 256:
            yield bytes([ca])


def DecodeCore():
    flag = True
    cur_encoding = ''
    while flag:
        inp = input("从文本文件(F)\n我自己输入/粘贴到控制台(P)\n读取剪贴板(R)\n直接退出(E)\n")
        if inp == "F" or inp == "f":
            FiName = input("请输入文件名(*.txt):")
            with open(FiName, 'rb') as f:
                cur_encoding = chardet.detect(f.read())['encoding']
                if cur_encoding == 'GB2312':
                    cur_encoding = 'GBK'
            Tfile = open(FiName, encoding=cur_encoding)
            tst = Tfile.read()
            Tfile.close()
            flag = False
        elif inp == "P" or inp == "p":
            tst = input("请输入核心价值编码:\n")
            flag = False
        elif inp == "R" or inp == "r":
            tst = GetText()
            flag = False
        elif inp == "E" or inp == "e":
            exit(0)
        else:
            print("输入有误！请重新选择:")
    #txtfi = ''.join(valueDecode(tst)).decode('utf-8')
    #cur_encoding = chardet.detect(b''.join(valueDecode(tst)))['encoding']
    txtfi = b''.join(valueDecode(tst))
    outo = input("输出到文本文件(F)\n拷贝到剪贴板(C)\n直接打印(P)\n退出(E)\n")
    if outo == "F" or outo == "f":
        OutName = input("请键入输出文件名(*.*):")
        Pfile = open(OutName, "w", encoding=cur_encoding)
        Pfile.write(txtfi.decode('utf-8'))
        Pfile.close()
        print("输出完成，请打开同目录下 " + OutName + " 文件查看")
    elif outo == "P" or outo == "p":
        print(txtfi.decode('utf-8'))
    elif outo == "C" or outo == "c":
        SetText(txtfi.decode('utf-8'))
    elif outo == "E" or outo == "e":
        exit(0)
    else:
        print("输入有误！")


if __name__ == "__main__":
    logger = logging.getLogger("chardet")
    logger.setLevel(logging.INFO)
    print("社会主义核心价值编码程序")
    print("提示：\n只输入文件名将会操作同目录下文件\n若要使用其他位置的文件，\n请输入绝对或相对路径再输入文件名.\n")
    while True:
        cmd = input("请选择:\n编码(B)\n解码(D)\n清屏(C)\n退出(E)\n")
        if cmd == "B" or cmd == "b":
            EncodeCore()
        elif cmd == "D" or cmd == "d":
            DecodeCore()
        elif cmd == "E" or cmd == "e":
            exit(0)
        elif cmd == "C" or cmd == "c":
            os.system("cls")
        else:
            print("输入非法！请重新选择!")