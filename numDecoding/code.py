# -*- coding: utf-8 -*-
"""
Created on Mon May 21 20:51:20 2018

@author: lwang
"""

def numDecodings(s):
    """
    :type s: str
    :rtype: int
    """
    dp = [0]*len(s)
    for i in range(len(s)):
        if i == 0:
            if s[i]>="1" and s[i]<="9":
                dp[i] += 1
        else:                
            if s[i]>="1" and s[i]<="9":
                dp[i] += dp[i-1]
            
            if s[i-1:i+1]>="10" and s[i-1:i+1]<="26":
                if i>=2:
                    dp[i] += dp[i-2]
                else:
                    dp[i] += 1
    return dp[-1]