#!/usr/bin/env python

import os

def home():
	os.popen("adb shell input keyevent 3")


def back():
	os.popen("adb shell input keyevent 4")

def lockscreen():
	os.popen("adb shell input keyevent 26")

def phonecall():
	os.popen("adb shell input keyevent 5")

def volumeup():
	os.popen("adb shell input keyevent 24")

def volumedown():
	os.popen("adb shell input keyevent 25")

def click(x,y):
	os.popen("adb shell input tap" + " "+str(x)+" "+str(y))
if __name__ == '__main__':
	back()