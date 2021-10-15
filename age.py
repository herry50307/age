# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 16:21:29 2021

@author: DSC Handsome
"""

drive= input ("請問你有沒有開過車: ")
if drive !="有" and drive !="沒有":
    print("只能輸入 有/沒有")
    raise SystemExit
    
age=int(input("請問你的年齡: "))

if drive == "有" :
    if age>= 18:
        print("你通過測驗了")
    else:
        print("你不應該開車")
elif drive == "沒有":
    if age>= 18:
        print("可以去考駕照了")
    else:
        print("再等幾年就可以去考了")
else:
    print("只能回答有或沒有")
        