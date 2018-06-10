# -*- coding: utf-8 -*-
"""
Created on Sat Jun 09 22:27:39 2018

@author: lwang
"""


def minWindow(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """        
    
    minlen = 2147483649
    res= ""
    
    pool = list(t)
    targ = set(t)
    if s:
        stack = []
        index = []        
        for i in range(len(s)):                
            if s[i] in targ:
                stack.append(s[i])
                index.append(i)           
                j = len(stack)-1
                while pool and j>=0:
                    if stack[j] in pool:
                        pool.remove(stack[j])
                    j -= 1                            
                if not pool:
                    if minlen>index[-1]-index[j+1]+1:
                        minlen = index[-1]-index[j+1]+1
                        res = s[index[j+1]:index[-1]+1]
                    while index and index[-1]-index[0]+1>=minlen:
                        index.pop(0)
                        stack.pop(0)
                        
                pool = list(t)                    
                            
    return res             
                