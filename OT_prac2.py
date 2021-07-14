# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 13:52:38 2021

@author: vedika
"""

#COST MINIMUM METHOD

import numpy as np
 

"""
#transportation problem input
supply = list(map(int,input("Enter the supply (give space between each value): ").strip().split()))
demand = list(map(int,input("Enter the demand (give space between each value): ").strip().split()))
cost = list(map(int,input("Enter the cost (give space between each value): ").strip().split()))
cost = (np.asarray(cost)).reshape((n,m))
c = cost.copy().tolist()
"""

#problem statement
supply = [11,13,19] #i
demand = [6,10,12,15] #j
c = [[21,16,15,3],
     [17,18,14,23],
     [32,27,18,41]]
tot_cost = 0
print("\nTRANSPORTATION PROMLEM IS AS FOLLOWS :\nsupply=",supply,"\ndemand=",demand,"\ncost=",c,
      "\n\n\nITERATIONS OF COST MINIMUM METHOD ARE AS FOLLOWS :")

#checked if balanced problem
if (sum(supply)!=sum(demand)):
    print("\nIts not a balanced problem. Please enter values again.")
else:
    while(sum(demand)!=0):
        n,m = np.shape(c)
        mini  = np.amin(c)
        
        #find minimum cij
        i=0
        j=0
        for a in range(n): 
            for b in range(m): 
                if(c[a][b] == mini):
                    i=a
                    j=b
                    break
        
        if (supply[i]<demand[j]):
            k=supply[i]
            demand[j]= demand[j]-supply[i]
            supply[i]=0
            
        elif (supply[i]>demand[j]):
            k=demand[j]
            supply[i]= supply[i]-demand[j]
            demand[j]=0
            
        else:
            k=demand[j]
            supply[i]=0
            demand[j]=0
            
        tot_cost = tot_cost + (mini*k) 
        
        if (supply[i]==0):
            c = np.delete(c, i, 0)
            supply.pop(i)
        if (demand[j]==0):
            c = np.delete(c, j, 1)
            demand.pop(j)
        
        print("minimum=",mini,"\nupdated supply=",supply,"\nupdated demand=",demand,"\nupdated cost=\n",c,"\n")

print("\n\nRESULT :\nTherefore total transportation cost is Rs.",tot_cost)     
      