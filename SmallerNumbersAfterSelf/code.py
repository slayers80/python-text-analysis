# -*- coding: utf-8 -*-
"""
Created on Wed May 30 13:24:36 2018

@author: lwang
"""

def countSmaller(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    
    if nums:            
        res = [0]*len(nums)
        for i in range(len(nums)):
            count = 0
            for j in range(i,len(nums)):
                count += nums[j]<nums[i]
            res[i] = count
        return res
    else:
        return []