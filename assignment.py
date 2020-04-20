# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 11:18:49 2020

@author: Mahidhar
"""
import math


def func1():
    res = []
    for i in range(2000, 3201):
        if i % 7 == 0 and i % 5 != 0:
            res.append(str(i))
    return ', '.join(res)


def func2():
    fname = input("Please enter your first name: ")
    lname = input("Please enter your last name: ")
    return fname[::-1] + " " + lname[::-1]


def func3():
    d = 12
    r = d/2;
    V = (4/3)*(math.pi)*(r**3)
    return V
  
    
if __name__ == "__main__":
    out1 = func1()
    print(out1)
    out2 = func2()
    print(out2)
    out3 = func3()
    print(out3)