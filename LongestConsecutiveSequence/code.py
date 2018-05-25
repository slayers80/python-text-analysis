# -*- coding: utf-8 -*-
"""
Created on Thu May 24 17:10:17 2018

@author: lwang
"""

def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums)<=1:
        return len(nums)
    
    lens = []
    flag = False
    nums.sort()
    curlen = 1
    for i in range(1,len(nums)):
        if nums[i]-nums[i-1]==1:
            if flag:
                curlen += 1
            else:
                curlen += 1
                flag = True
        else:
            if flag:
                if nums[i-1]!=nums[i]:
                    flag = False
                    lens.append(curlen)
                    curlen = 1
    lens.append(curlen)
    return max(lens) if lens else 0



def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums = set(nums)
    best = 0
    for x in nums:
        if x - 1 not in nums:
            y = x + 1
            while y in nums:
                y += 1
            best = max(best, y - x)
    return best