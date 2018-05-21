# -*- coding: utf-8 -*-
"""
Created on Mon May 21 18:39:20 2018

@author: lwang
"""

def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """ 
    counter = {}
    del_inds = []
    for i in range(len(nums)):            
        num = nums[i]
        if num not in counter:
            counter[num] = 1
        elif counter[num]<=2:
            counter[num] += 1
        else:
            del_inds.append(i)
    for i in sorted(del_inds, reverse=True):
        del nums[i]
            
    dic = {nums[i]:i for i in range(len(nums))}
    res = set()
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if -nums[i]-nums[j] in dic:
                k = dic[-nums[i]-nums[j]]                    
                if k != i and k != j:
                    entry = sorted([-nums[i]-nums[j], nums[i], nums[j]])
                    if tuple(entry) not in res:
                        res.add(tuple(entry))
    return list(res)