# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 09:56:43 2018

@author: lwang
"""

def partition(s):
    """
    :type s: str
    :rtype: List[List[str]]
    """
    def isPalindrome(string):
        if len(string) == 0:
            return True
        
        l,h = 0, len(string)-1
        while l<h:
            if string[l] == string[h]:
                l += 1
                h -= 1
            else:
                return False
            
        return True
    
    if len(s)<=1:
        return [[s]]
            
    
    result = []
    if isPalindrome(s):
        result.append([s])
        
    frontiers = [[s]]
    while frontiers:
        nextlevel = []
        for node in frontiers:
            laststr = node.pop()
            for i in range(1,len(laststr)):                    
                if isPalindrome(laststr[0:i]):                        
                    nextlevel.append(node+[laststr[0:i]]+[laststr[i:]])
                    if isPalindrome(laststr[i:]):
                        result.append(node+[laststr[0:i]]+[laststr[i:]])
        frontiers = nextlevel
    
    return result


def partition2(s):
    """
    :type s: str
    :rtype: List[List[str]]
    """
    return [[s[:i]] + rest
        for i in xrange(1, len(s)+1)
        if s[:i] == s[i-1::-1]
        for rest in partition2(s[i:])] or [[]]
                    