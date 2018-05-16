# -*- coding: utf-8 -*-
"""
Created on Tue May 15 22:18:49 2018

@author: lwang
"""

def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    res = []
    if matrix:
        m, n = len(matrix), len(matrix[0])
        l = m/2 if not m%2 else m/2+1
        p = n/2 if not n%2 else n/2+1
        
        for r in range(min(l,p)):                
            res += matrix[r][r:n-r]
            for i in range(r+1,m-r-1):
                res += [matrix[i][n-r-1]]
            if m-r-1>r:
                res += matrix[m-r-1][-1-r:-n+r-1:-1]
            if r<n-r-1:
                for i in range(m-r-2, r, -1):
                    res += [matrix[i][r]]
    return res


def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    return matrix and list(matrix.pop(0)) + self.spiralOrder(zip(*matrix)[::-1])