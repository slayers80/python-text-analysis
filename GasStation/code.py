# -*- coding: utf-8 -*-
"""
Created on Fri May 11 22:35:27 2018

@author: lwang
"""

def canCompleteCircuit(gas, cost):
    """
    :type gas: List[int]
    :type cost: List[int]
    :rtype: int
    """
    
    
    csum = 0
    total = 0
    start = 0
    for i in range(len(gas)):
        csum = csum + gas[i] - cost[i]
        if csum < 0:
            total = total+csum
            csum = 0
            start = i+1                         
                
    return start if (total+csum)>=0 else -1