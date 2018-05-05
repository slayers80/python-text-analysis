# -*- coding: utf-8 -*-
"""
Created on Thu May 03 18:57:10 2018

@author: lwang
"""
import random
# {'apple':3, 'banana':5, 'orange':2}

def fruitprint(dic):
    
    fruits = []
    cumsum = [0]    
    for key, value in dic.iteritems():
        fruits.append(key)
        cumsum.append(cumsum[-1]+value)
    
    randnum = random.randint(1,cumsum[-1])
    print cumsum, randnum
    
    for i in range(1,len(cumsum)):
        if cumsum[i-1]<randnum<=cumsum[i]:
            print fruits[i-1]