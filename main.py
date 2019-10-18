#!/usr/bin/env python
#-*- coding: UTF-8 -*-
'''
主程序
'''
 
import qrcode
 
while (True):
    print ("1: qrcode 创建")
    print ("2: qrcode 识别")
    print (u"3: 退出")
    select=int(input(u"请选择: "))
    if select == 1:
        qrcode.erzeugen()
    elif select == 2:
        result=qrcode.lesen().strip()
        print (result)
    elif select == 3:
        print (u"完成程序...")
        break
