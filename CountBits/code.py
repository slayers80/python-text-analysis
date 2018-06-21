# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 22:19:54 2018

@author: lwang
"""

def countBits(num):
    """
    :type num: int
    :rtype: List[int]
    """
    dp = [0]*(num+1)
    offset = 1
    for i in range(1,num+1):
        if i<offset*2:
            dp[i] = dp[i-offset]+1
        else:
            offset *= 2                
            dp[i] = dp[i-offset]+1
            
    return dp