# -*- coding: utf-8 -*-
"""
Created on Sat May 05 00:25:57 2018

@author: lwang
"""

def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    
    def dfs(prefix, suffix):            
        if suffix in worddic:
            return True
        
        for i in range(len(suffix)-1):
            if suffix[:i+1] in worddic:
                next_prefix = prefix+suffix[:i+1]
                if next_prefix not in visited:
                    visited[next_prefix] = 1
                    if dfs(next_prefix, suffix[i+1:]):
                        return True
        return False
    
    if not s or not wordDict:
        return False        
    
    
    worddic = {s:0 for s in wordDict}
    visited = {}

    return dfs('', s)




def wordBreak2(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    
    d = [False]*len(s)
    
    for i in range(len(s)):
        for w in wordDict:                
            if w==s[i+1-len(w):i+1] and (d[i-len(w)] or i-len(w)==-1):
                d[i] = True
    print d                   
    return d[-1]