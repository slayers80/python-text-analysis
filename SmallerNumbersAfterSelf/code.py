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
    
    
def countSmaller2(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    

    def sort(enum):
        half = len(enum) / 2
        if half:
            left, right = sort(enum[:half]), sort(enum[half:])
            for i in range(len(enum))[::-1]:
                if not right or left and left[-1][1] > right[-1][1]:
                    smaller[left[-1][0]] += len(right)
                    enum[i] = left.pop()
                else:
                    enum[i] = right.pop()
        return enum
    smaller = [0] * len(nums)
    sort(list(enumerate(nums)))
    return smaller