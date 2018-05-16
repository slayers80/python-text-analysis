# -*- coding: utf-8 -*-
"""
Created on Tue May 15 21:05:15 2018

@author: lwang
"""

def exist(board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """        
    
    def dfs(board, coord, subword, m, n, visited):
        #print coord, subword, visited
        if len(subword) == 1:
            if board[coord[0]][coord[1]] == subword:
                return True
            else:
                return False
        if not (board[coord[0]][coord[1]] == subword[0]):
            return False
        else:                
            if coord not in visited:
                visited += [coord]
                if coord[0]>0:
                    x = coord[0]-1
                    y = coord[1]
                    if [x,y] not in visited:                        
                        if dfs(board, [x,y], subword[1:], m, n, visited):
                            return True                        
                if coord[0]<m-1:
                    x = coord[0]+1
                    y=coord[1]     
                    if [x,y] not in visited:                        
                        if dfs(board, [x,y], subword[1:], m, n, visited):
                            return True
                if coord[1]>0:
                    x = coord[0]
                    y = coord[1]-1
                    if [x,y] not in visited:                        
                        if dfs(board, [x,y], subword[1:], m, n, visited):
                            return True
                if coord[1]<n-1:
                    x = coord[0]
                    y = coord[1]+1   
                    if [x,y] not in visited:                        
                        if dfs(board, [x,y], subword[1:], m, n, visited):
                            return True
                visited.remove(coord)
    
    
    m = len(board)
    if not m:
        return False
    n = len(board[0])
    if not n:
        return False
    
    for i in range(m):
        for j in range(n):
            visited = []        
            if dfs(board, [i,j], word, m, n, visited):
                return True
    return False