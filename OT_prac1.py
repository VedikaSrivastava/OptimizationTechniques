# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 14:58:15 2021

@author: vedika
"""

R = 0.618
print ("Enter the following values\na=")
a = int(input())
print ("b=")
b = int(input())
print ("tolerance(in %)=")
e = (float(input()))/100
print ("max_iter=")
max_iter = int(input())

def cal_function(x):
    fx = (2*x)-(1.75*x**2)+(1.1*x**3)-(0.25*x**4)
    return fx

for k in range(1,max_iter):
    x1 = a + R*(b-a)
    x2 = b - R*(b-a)
    f1 = cal_function(x1)
    f2 = cal_function(x2)
    
    print("\n\nItertaion ",k,"\nx1 = ",x1,"\nx2 = ",x2,"\n(x1-x2) = ",(x1-x2))
    
    if ((x1-x2)<e):
        print("\n\nMAXIMA OF THE FUNCTION IS (",a,", ",b,")")
        break
    
    if (f1>f2):
        a=x2
        
    else:
        b=x1
        