# -*- coding: utf-8 -*-
"""
Created on Mon May 14 19:24:37 2018

@author: lwang
"""

def maxSlidingWindow(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    if not nums:
        return []
    
    res=[]
    for i in range(len(nums)-k+1):
        if i == 0:
            max_val = nums[0]
            max_loc = 0
            for j in range(1,k):
                if nums[j] >= max_val:
                    max_val = nums[j]
                    max_loc = j
            res.append(max_val)
        else:
            if i-1<max_loc:
                if max_val<=nums[i+k-1]:
                    max_val = nums[i+k-1]
                    max_loc = i+k-1
                
            else:
                max_val = nums[i]
                max_loc = i
                for j in range(i+1,i+k):
                    if nums[j] >= max_val:
                        max_val = nums[j]
                        max_loc = j
            res.append(max_val)
            
    return res