# -*- coding: utf-8 -*-
"""
Created on Sat May 19 22:11:38 2018

@author: lwang
"""

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    maxlen = 0    
    substr = ""        
    for i in range(len(s)):            
        ind = substr.find(s[i])               
        if ind == -1:                  
            substr += s[i]
            if maxlen < len(substr):
                maxlen = len(substr)
        else:
            substr = substr[ind+1:]+s[i]                
        
    return maxlen