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
    
    rarestfreq = min(dic.itervalues())
    if rarestfreq>=k:
        return len(s)
    
    else:
        for a in dic.iteritems():
            if a[1] == rarestfreq:
                rarestletter = a[0]
        
        print rarestletter
        m = []
        for s1 in s.split(rarestletter):
            m.append(LongestSubstring(s1,k))
        if max(m)>=k:
#            print max(m)
            return max(m)
        else:
            return 0