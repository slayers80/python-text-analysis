# -*- coding: utf-8 -*-
"""
Created on Wed Jun 06 07:53:08 2018

@author: lwang
"""

def largestRectangleArea(heights):
    """
    :type heights: List[int]
    :rtype: int
    """
    if not heights:
        return 0
    
    maxarea = 0
    for i in range(len(heights)):
        areas = [heights[i]]
        for j in range(i):
            areas.append(min(heights[j:i+1])*(i-j+1))
        maxarea = max(maxarea, max(areas))
    return maxarea


def largestRectangleArea2(heights):
    """
    :type heights: List[int]
    :rtype: int
    """
    heights.append(0)
    stack = [-1]
    ans = 0
    for i in xrange(len(heights)):
        while heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i - stack[-1] - 1
            ans = max(ans, h * w)
        stack.append(i)
    
    return ans