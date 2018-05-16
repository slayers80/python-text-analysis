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
    
    def dfs(board, coord, subword, m, n):
        #print coord, subword, visited
        if len(subword) == 1:
            if board[coord[0]][coord[1]] == subword:
                return True
            else:
                return False
        if not (board[coord[0]][coord[1]] == subword[0]):
            return False
        else:                
            board[coord[0]][coord[1]] = '#'
            if coord[0]>0:
                x = coord[0]-1
                y = coord[1]                        
                if dfs(board, [x,y], subword[1:], m, n):
                    return True                        
            if coord[0]<m-1:
                x = coord[0]+1
                y=coord[1]                                                  
                if dfs(board, [x,y], subword[1:], m, n):
                    return True
            if coord[1]>0:
                x = coord[0]
                y = coord[1]-1                        
                if dfs(board, [x,y], subword[1:], m, n):
                    return True
            if coord[1]<n-1:
                x = coord[0]
                y = coord[1]+1                           
                if dfs(board, [x,y], subword[1:], m, n):
                    return True
            board[coord[0]][coord[1]] = subword[0]
    
    m = len(board)
    if not m:
        return False
    n = len(board[0])
    if not n:
        return False
    
    for i in range(m):
        for j in range(n):                  
            if dfs(board, [i,j], word, m, n):
                return True
    return False