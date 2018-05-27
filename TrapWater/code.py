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