# -*- coding: utf-8 -*-
"""
Created on Fri Jun 01 23:14:27 2018

@author: lwang
"""

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.array = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if not self.array:
            self.array.append(num)
        else:
            lo, hi = 0, len(self.array)-1            
            while lo<=hi:
                mid = (lo+hi)/2
                if self.array[mid]<num:
                    lo = mid+1
                elif self.array[mid]>num:
                    hi = mid-1
                else:
                    self.array.insert(mid, num)
                    return
            self.array.insert(min(lo, hi)+1,num)

    def findMedian(self):
        """
        :rtype: float
        """
        if not self.array:
            return None
        else:
            l = len(self.array)            
            return self.array[l/2] if l%2==1 else sum(self.array[l/2-1:l/2+1])/2.


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()