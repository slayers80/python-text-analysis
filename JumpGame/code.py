# -*- coding: utf-8 -*-
"""
Created on Sun May 13 13:18:17 2018

@author: lwang
"""

def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    N = len(nums)
    dp = [0]*N
    dp[-1] = 1
    minind = N-1
    for i in range(1,N):
        start = N-i-1
        end = start+nums[start]             
        if end >= minind:
            dp[start] = 1
            if minind>start:
                minind = start             
            
    #print dp
    return bool(dp[0])