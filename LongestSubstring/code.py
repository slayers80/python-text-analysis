# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 20:13:40 2018

@author: lwang
"""

def LongestSubstring(s, k):
    
    if len(s)<k:
        return 0

    dic = {}
    for ch in s:
        if ch in dic:
            dic[ch] += 1
        else:
            dic[ch] = 1

    if min(dic.itervalues())>=k:
        return len(s)  
        
    for key in dic:
        if dic[key] < k:
            
            m = []
            for s1 in s.split(key):
                m.append(longestSubstring(s1,k))
            if max(m)>=k:
                return max(m)
            else:
                return 0
        
        
def longestSubstring(s, k):
    for c in set(s):
        if s.count(c) < k:
            return max(longestSubstring(t, k) for t in s.split(c))
    return len(s)        