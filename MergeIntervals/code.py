# -*- coding: utf-8 -*-
"""
Created on Wed May 02 21:41:41 2018

@author: lwang
"""

def merge(intervals):
    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    """        
    if intervals:
        intervals = sorted(intervals, key=lambda i: i.start)
        
        lastinterval = intervals[0]            
        for interval in intervals[1:]:                    
            if lastinterval.end>=interval.end:
                intervals.remove(interval)
            elif lastinterval.end>=interval.start:
                lastinterval.end = interval.end                    
                intervals.remove(interval)
            else:                    
                lastinterval = interval   
                
    return intervals