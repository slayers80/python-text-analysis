# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 07:36:51 2018

@author: lwang
"""

def firstMissingPositive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if nums:
        n = set(nums)
        maxnum = max(nums)
        for i in range(1,maxnum):
            if i not in n:
                return i
        return maxnum+1
    return 1