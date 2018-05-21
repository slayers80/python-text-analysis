# -*- coding: utf-8 -*-
"""
Created on Sun May 20 22:04:54 2018

@author: lwang
"""

def largestNumber(nums):
    """
    :type nums: List[int]
    :rtype: str
    """
    max_len = len(list(str(max(nums))))
    nums_list = [str(num)+(max_len*str(num))[:(max_len-len(str(num)))] for num in nums]        
    
    inds = sorted(range(len(nums_list)),key=lambda x:nums_list[x])
    inds = inds[::-1]
    
    res = ""
    for i in range(len(inds)-1):            
        if nums_list[inds[i]]==nums_list[inds[i+1]]:
            str1 = str(nums[inds[i]])
            str2 = str(nums[inds[i+1]])
            if int(str1+str2) < int(str2+str1):
                nums[inds[i]], nums[inds[i+1]] = nums[inds[i+1]], nums[inds[i]]
        res += str(nums[inds[i]])
    res += str(nums[inds[-1]])
    
    
    i=0
    if len(res)>1:
        for i in range(len(res)):
            if res[i]!='0' or i==len(res)-1:
                break
    
    return res[i:]