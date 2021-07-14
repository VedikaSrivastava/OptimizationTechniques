# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 14:08:44 2021

@author: vedika
"""

#take input
at = int(input("Enter average arrival time between two stations (in sec) : "))
st = int(input("Enter average service time(in sec) : "))

lamda = (1/at)*60
m = (1/st)*60

print("\nAverage queue length (Lq) = ",((lamda**2)/(m*(m-lamda)))," workers")

print("Average length of non-empty queues (Lb) = ", (m/(m-lamda))," workers")

print("Average no. of workers in the system (Ls) = ", (lamda/(m-lamda))," workers")

print("Mean waiting time of an arrival (Wq) = ",(lamda/(m*(m-lamda)))," minutes")

print("Average waiting time of an arrival (Pw) = ",(1/(m-lamda))," minutes")

#prob room remains idle,P0
P0 = 1 - (lamda/m)
idle_t = P0 * 8 * 0.75
waiting_t = (lamda/(m*(m-lamda))) * (1/60) * (8*60) * 4
if waiting_t>idle_t:
    print("Since waiting time exceeds idle time, Additional Attendant is needed")
else:
    print("Since idle time exceeds waiting time,Additional Attendant is not needed")
