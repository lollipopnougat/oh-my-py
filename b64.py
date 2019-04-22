# -*- coding:UTF-8 -*-
# b64.py --- binary file 2 base64 and basr64 2 binary file
''' 
-------------------------------

请先安装依赖 pywin32 !
请先安装依赖 pywin32 !!
请先安装依赖 pywin32 !!!

管理员身份进入powershell 
键入 "pip install pywin32" 
(当然前提是你得安好pip并配置好环境变量)

注意！ 本脚本在python 3.7.1 版本下良好运行， 低于此版本的尚未进行测试

封掣 2019.2.5
-------------------------------
'''
# win32con 即win api常量的python实现，C/C++一般都是在windows.h内大写的宏定义
import win32con
import win32clipboard as w
import base64
import os


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


# 原理为python使用标准库base64将二进制编码的数据转码为base64编码
def EncodeB64():
    name = input("输入二进制文件名(*.*): ",)
    f = open(name, "rb")  
    ls_f = base64.b64encode(f.read())  
    ls_str = str(ls_f, encoding = "utf-8")
    f.close()
    # print(type(ls_f))
    flag = True
    while flag:
    	inp = input("拷贝到剪贴板(C)\n打印到控制台(P)\n写入txt文件(W)\n直接退出(E)\n")
    	if inp == "C" or inp == "c":
        	SetText(ls_str)
        	flag = False
    	elif inp == "P" or inp == "p":
            os.system("cls")
            print(ls_f)
            flag = False
    	elif inp == "E" or inp == "e":
            exit(0)
    	elif inp == "W" or inp == "w":
            FiNa = input("请输入文件名(*.txt):")
            Tfi = open(FiNa, "w") # 基础文件操作
            Tfi.write(ls_str)
            Tfi.close()
            print("写入完成，请打开同目录下的 " + FiNa + "查看.")
            flag = False
    	else:
            print("输入有误！请重新选择:")

def DecodeB64():
    flag =True
    while flag:
        inp = input("从文本文件(F)\n我自己粘贴/输入到控制台(P)\n读取剪贴板(R)\n直接退出(E)\n")
        if inp == "F" or inp == "f":
            FiName = input("请输入文件名(*.txt):")
            Tfile = open(FiName)
            tst = Tfile.read()
            Tfile.close()
            flag = False
        elif inp == "P" or inp == "p":
            tst = input("请输入Base64编码:\n")
            flag = False
        elif inp == "R" or inp == "r":
            tst = GetText()
            flag = False
        elif inp == "E" or inp == "e":
            exit(0)
        else:
            print("输入有误！请重新选择:")
    img = base64.b64decode(tst)
    OutName = input("请键入输出文件名(*.*):") 
    Pfile = open(OutName,"wb") 
    Pfile.write(img)  
    Pfile.close()
    print("输出完成，请打开同目录下 " + OutName + " 文件查看")


def main():
    print("Base64、二进制串相互转换脚本")
    print("提示：\n只输入文件名将会操作同目录下文件\n若要使用其他位置的文件，\n请输入绝对或相对路径再输入文件名.\n")
    while True:
        cmd = input("请选择:\n编码(B)\n解码(D)\n清屏(C)\n退出(E)\n")
        if cmd == "B" or cmd == "b":
            EncodeB64()
        elif cmd == "D" or cmd == "d":
            DecodeB64()
        elif cmd == "E" or cmd == "e":
            exit(0)
        elif cmd == "C" or cmd == "c":
            os.system("cls")
        else:
            print("输入非法！请重新选择!")

main()
input("任意键退出")


