# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 13:48:23 2021

@author: vedika
"""
import numpy as np
try:
    #user input
    print("Number of machines = 2")
    n_job = int(input('Enter the number of jobs = '))
    pt_m1 = list(map(int,input("Enter the processing times of Machine 1(give space between each value):\n ").strip().split()))
    pt_m2 = list(map(int,input("Enter the processing times of Machine 2(give space between each value):\n ").strip().split()))
except:
    print("Please check your input.")
    
pt_m1_copy = pt_m1.copy()
pt_m2_copy = pt_m2.copy()
seq = [0] * n_job
head = 0
tail = n_job-1

def remov(e_idx,l1=pt_m1_copy,l2=pt_m2_copy):
    l1.pop(e_idx)
    l2.pop(e_idx)


#Johnson's algo
while (head <= tail):
    min_m1 = min(pt_m1_copy)
    min_m2 = min(pt_m2_copy)
    min_c = min(min_m1,min_m2)
    
    if(min_c == min_m1):
        n = pt_m1_copy.count(min_c)
        if (n == 1):
            seq[head] = pt_m1.index(min_c) + 1
            head = head+1
            remov(pt_m1_copy.index(min_c))
        else:
            seq2 = list()
            for x in range(len(pt_m1_copy)):
                if pt_m1_copy[x]==min_c:
                    seq2.append(pt_m2_copy[x])
            
            for x in range(len(seq2)):
                if(np.shape(seq2) == (1,)):
                    m = seq2[0]
                else:
                    m = min(seq2)
                    seq2.pop(x)
                seq[head] = pt_m2.index(m)+1
                head = head + 1
                remov(pt_m2_copy.index(m))
            
    
    else:
        n = pt_m2.count(min_c)
        if (n == 1):
            seq[tail] = pt_m2.index(min_c) + 1
            tail = tail - 1
            remov(pt_m2_copy.index(min_c))
        else:
            seq2 = list()
            for x in range(len(pt_m2_copy)):
                if pt_m2_copy[x]==min_c:
                    seq2.append(pt_m1_copy[x])
            
            for x in range(len(seq2)):
                if(np.shape(seq2) == (1,)):
                    m = seq2[0]
                else:
                    m = min(seq2)
                    seq2.pop(x)
                seq[tail] = pt_m1.index(m) + 1
                tail = tail - 1
                remov(pt_m1_copy.index(m))
                
print("\nThe optimal sequence is \n", seq)