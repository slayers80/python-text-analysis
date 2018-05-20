# -*- coding: utf-8 -*-
"""
Created on Sat May 19 20:48:46 2018

@author: lwang
"""

def myPow(x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """
    if n<0:
        return (1/x)*self.myPow(1/x,-n-1)
    if n == 0:
        return 1
    if n == 1:
        return x
    if n%2 == 0:
        return self.myPow(x*x, n/2)
    else:
        return x*self.myPow(x*x, (n-1)/2)