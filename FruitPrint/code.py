# -*- coding: utf-8 -*-
"""
Created on Thu May 03 18:57:10 2018

@author: lwang
"""
import random
# {'apple':30, 'banana':5, 'orange':12}

def fruitprint(dic):
    
    fruits = []
    cumsum = [0]    
    for key, value in dic.iteritems():
        fruits.append(key)
        cumsum.append(cumsum[-1]+value)
    
    randnum = random.randint(1,cumsum[-1])
        
    for i in range(1,len(cumsum)):
        if cumsum[i-1]<randnum<=cumsum[i]:
            print fruits[i-1]
            
            
from random import randint            
def printFruit(dic):

    if dic:
        fruit = []
        csum = [0]
        for key, val in dic.items():
            fruit.append(key)
            csum.append(csum[-1]+val)
            
        r = randint(1,csum[-1])
        
    #    for i in range(len(dic)):
    #        if cumsum[i]<randnum<=cumsum[i+1]:
    #            print fruit[i]
        lo, hi = 0, len(csum)-1
        while lo<hi:
            mid = (lo+hi)/2        
            if r<csum[mid]:
                hi = mid
            elif r>csum[mid]:
                lo = mid+1
            else:
                print fruit[mid-1]
                return
        
        print fruit[lo-1]
    

def binarySearch(nums, target):
    
    lo, hi = 0, len(nums)-1
    while lo<hi:
        mid = (lo+hi)/2        
        if target<nums[mid]:
            hi = mid
        elif target>nums[mid]:
            lo = mid+1
        else:
            print nums[mid]
            break
    if lo==hi:
        print nums[lo-1]
        
        
def printFruit2(dic):

    if not dic:
        print ''        
    
    else:
        csum = 0
        for key, val in dic.items():
            csum = csum+val
            dic[key] = csum
#        print dic
        r = randint(1, csum)
        
        fruit = ''
        minnum = csum
        for key, val in dic.items():            
            if val>=r:
                if val-r<minnum:
                    minnum = val-r
                    fruit = key
        print fruit
                
        

dic = {} # {'apple':30, 'banana':5, 'orange':12}

for i in range(20):
#    dic = {'apple':10, 'banana':5, 'orange':2,'peach':1}
    printFruit(dic)
   