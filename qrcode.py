#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import os, signal, subprocess
from picamera import PiCamera 

strfile1 = "qrcode"

def erzeugen():
    text=input(u"enter text QRCode: ")
    os.system("qrencode -o "+strfile1+".png '"+text+"'")
    print (u"QRCode in: "+strfile1+".png")
    
def lesen():
    os.system("raspistill -w 320 -h 240 -o /home/pi/Desktop/cam/qrcode/image.jpg")
    print (u"raspistill finished")
    #zbarcam=subprocess.Popen("zbarcam --raw --nodisplay /dev/video0", stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
    #print u"zbarcam started successfully..."
    #qrcodetext=zbarcam.stdout.readline()
    zbarcam=subprocess.Popen("zbarimg --raw /home/pi/Desktop/cam/qrcode/image.jpg", stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
    qrcodetext=zbarcam.stdout.readline().decode()
    if qrcodetext != "":
        #print (qrcodetext)
        pass
    else:
        print (u"qrcodetext 为空")
        
    #os.killpg(zbarcam.pid, signal.SIGTERM)
    print (u"zbarcam stopped successfully...")
    qrresult = f"QRCode: {qrcodetext}"
    return (qrresult)