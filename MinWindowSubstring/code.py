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
    targ = set(t)
    
    minlen = 2147483649
    res= ""
    if s:
        stack = []
        index = []        
        for i in range(len(s)):
            if s[i] in targ:
                stack.append(s[i])
                index.append(i)
                if set(stack)==targ:
                    for j in range(len(stack)-1,-1,-1):
                        if set(stack[j:])==targ:
                            if minlen>index[-1]-index[j]:
                                minlen = index[-1]-index[j]
                                res = s[index[j]:index[-1]+1]
                            while index and index[-1]-index[0]>=minlen:
                                index.pop(0)
                                stack.pop(0)
                            break
                            
    return res 