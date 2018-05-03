# -*- coding: utf-8 -*-
"""
Created on Wed May 02 20:31:31 2018

@author: lwang
"""
def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    def search(n):
        l, h = 0 ,len(nums)
        while l<h:
            c = (l+h)/2
            if nums[c] >= n:
                h = c
            else:
                l = c+1
        return l
    
    lo = search(target)
    return [lo, search(target+1)-1] if target in nums[lo:lo+1] else [-1, -1]