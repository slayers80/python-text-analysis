# -*- coding: utf-8 -*-
"""
Created on Sat May 19 20:02:38 2018

@author: lwang
"""

def wiggleSort(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """        
    
    
    nums1 = sorted(nums)
    
    nums[::2], nums[1::2] = nums1[(len(nums)+1)/2-1::-1], nums1[len(nums)-1:(len(nums)+1)/2-1:-1]