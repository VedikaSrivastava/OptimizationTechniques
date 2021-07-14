# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 14:55:50 2021

@author: vedika
"""

"""
Variable desciption :
    coins - stores the value of coins available
    n - stores the desired sum
    min_no_c - stores the minimum number of coins required to obtain desired sum - function variable
    min_c - stored the minimum number of coins required to obtain desired sum
"""

coins = list(map(int,input("Enter the coins (give space between each value):").strip().split()))
n = int(input("Enter the desired sum :"))

def min_coin(n):
    if n < 0:
        return float('inf')
    elif n == 0:
        return 0
    else:
        for val in coins:
            if coins.index(val)==0:
                min_no_c = min_coin(n-val)+1
            else:    
                min_no_c = min(min_coin(n-val)+1, min_no_c)
        return (min_no_c)

print("\nMinimum no. of coins required to obtain desired sum are ",min_coin(n))
