# -*- coding: utf-8 -*-
"""
Created on Mon May 28 20:00:32 2018

@author: lwang
"""

def longestIncreasingPath(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: int
    """
    visited = {}        
    def dfs(i,j, m,n,matrix):
        if (i,j) in visited:            
            return visited[(i,j)]
        else:
            l = []
            if i+1<m and matrix[i+1][j]>matrix[i][j]:
                l.append(1+dfs(i+1, j, m, n, matrix))
            else:
                l.append(1)
            if i-1>=0 and matrix[i-1][j]>matrix[i][j]:
                l.append(1+dfs(i-1, j, m, n, matrix))
            else:
                l.append(1)
            if j+1<n and matrix[i][j+1]>matrix[i][j]:
                l.append(1+dfs(i, j+1, m, n, matrix))
            else:
                l.append(1)
            if j-1>=0 and matrix[i][j-1]>matrix[i][j]:
                l.append(1+dfs(i, j-1, m, n, matrix))
            else:
                l.append(1)
            visited[(i,j)] = max(l)
            #print (i,j), visited[(i,j)]
            return max(l)
    if matrix:
        m,n = len(matrix), len(matrix[0])
        maxlen = 0
        for i in range(m):
            for j in range(n):
                maxlen = max(maxlen, dfs(i,j,m,n,matrix))
                #print maxlen
        return maxlen
    else:
        return 0
    

def longestIncreasingPath2(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: int
    """
    def dfs(i, j):
        if not dp[i][j]:
            val = matrix[i][j]
            dp[i][j] = 1 + max(
                dfs(i - 1, j) if i and val > matrix[i - 1][j] else 0,
                dfs(i + 1, j) if i < M - 1 and val > matrix[i + 1][j] else 0,
                dfs(i, j - 1) if j and val > matrix[i][j - 1] else 0,
                dfs(i, j + 1) if j < N - 1 and val > matrix[i][j + 1] else 0)
        return dp[i][j]

    if not matrix or not matrix[0]: return 0
    M, N = len(matrix), len(matrix[0])
    dp = [[0] * N for i in range(M)]
    return max(dfs(x, y) for x in range(M) for y in range(N))