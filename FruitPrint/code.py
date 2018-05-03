# -*- coding: utf-8 -*-
"""
Created on Thu May 03 18:57:10 2018

@author: lwang
"""
import random
# {'apple':3, 'banana':5, 'orange':2}

def fruitprint(dic):
    
    fruits = []
    nums = []
    for key, value in dic.iteritems():
        fruits.append(key)
        nums.append(value)
    
    cumsum = [0]
    tmp = 0
    for num in nums:
        tmp += num
        cumsum.append(tmp)    
    
    randnum = random.randint(1,cumsum[-1])
    print cumsum, randnum
    for i in range(1,len(cumsum)):
        if cumsum[i-1]<randnum<=cumsum[i]:
            print fruits[i-1]