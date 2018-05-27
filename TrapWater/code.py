# -*- coding: utf-8 -*-
"""
Created on Sun May 27 11:02:14 2018

@author: lwang
"""

def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    
    
    vol = 0
    
    if len(height)>2:            
        for i in range(1,len(height)-1):
            if i == 1:
                maxL, maxR = height[0], max(height[2:])
                level = min(maxL, maxR)
            else:
                if height[i-1] > maxL:
                    maxL = height[i-1]
                if height[i]==maxR:
                    maxR = max(height[i+1:])
                level = min(maxL, maxR)
            vol += level-height[i] if level>height[i] else 0
            
    return vol


def trap2(height):
    """
    :type height: List[int]
    :rtype: int
    """        
    
    if not height or len(height) < 3:
        return 0
    volume = 0
    left, right = 0, len(height) - 1
    l_max, r_max = height[left], height[right]
    while left < right:
        l_max, r_max = max(height[left], l_max), max(height[right], r_max)
        if l_max <= r_max:
            volume += l_max - height[left]
            left += 1
        else:
            volume += r_max - height[right]
            right -= 1
    return volume