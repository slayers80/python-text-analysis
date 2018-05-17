# -*- coding: utf-8 -*-
"""
Created on Wed May 16 20:51:15 2018

@author: lwang
"""

def maxProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    cprod1 = 1        
    first_neg = False
    max_seen = nums[0]-1
    for num in nums:
        if not num:
            cprod1 = 1                                
            first_neg = False
            if max_seen<0:
                max_seen = 0
        else:                
            cprod1 *= num    
            if first_neg:  # 2nd negative number and after                    
                cprod2 *= num                    
                if cprod2>0 and cprod2>max_seen:
                    max_seen = cprod2
                elif cprod1>0 and cprod1>max_seen:
                    max_seen = cprod1
                    
            else:      # first negative number
                if cprod1 > max_seen:
                    max_seen = cprod1
                    
                if num<0: 
                    first_neg = True                    
                    cprod2 = 1                    
            
    return max_seen



def maxProduct2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    maximum=big=small=nums[0]
    for n in nums[1:]:
        big, small=max(n, n*big, n*small), min(n, n*big, n*small)
        maximum=max(maximum, big)
    return maximum