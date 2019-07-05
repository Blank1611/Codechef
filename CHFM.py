# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 21:21:13 2019

@author: GRENTOR
"""
cases = int(input())
def const_mean(data_set):
    data = data_set.copy()
    org_mean = sum(data)/a
    data.sort()
    if len(data)%2 != 0:
        if org_mean == ((sum(data)-data[(len(data)+1)/2])/(a-1)):
            return (data_set.index(len(data)+1)/2)
    else:
        return None
        
    '''for i in range(len(data)):
        if org_mean == ((sum(data)-data[i])/(a-1)):
            return (data_set.index(data[i])+1)'''
        
        
for i in range(cases):
    a = int(input())
    data_set = list(map(int, input().split()))
    if len(set(data_set)) == 1:
        print(1)
    else:
        if const_mean(data_set):
            print(const_mean(data_set))
        else:
            print("Impossible")
        
    
