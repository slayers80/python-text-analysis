# -*- coding: utf-8 -*-
"""
Created on Fri May 25 09:05:25 2018

@author: lwang
"""

def solve(board):
    """
    :type board: List[List[str]]
    :rtype: void Do not return anything, modify board in-place instead.
    """
    if board:
        m = len(board)
        n = len(board[0])
        cands = [(0,i) for i in range(n)]+[(m-1,i) for i in range(n)]+[(i,0) for i in range(1,m-1)]+[(i,n-1) for i in range(1,m-1)]
        for (i,j) in cands:                
            if board[i][j] == 'O':                    
                front = [(i,j)]                    
                while front:
                    nex = set()
                    for i,j in front:
                        board[i][j] = 'S'                                 
                        if i+1<m and board[i+1][j]=='O':
                            nex.add((i+1, j))
                        if i-1>=0 and board[i-1][j]=='O':
                            nex.add((i-1, j))
                        if j+1<n and board[i][j+1]=='O':
                            nex.add((i, j+1))
                        if j-1>=0 and board[i][j-1]=='O':
                            nex.add((i, j-1))
                    front = list(nex)
                    
        for row in board:
            for i in range(n):
                if row[i] == 'O':
                    row[i] = 'X'
                if row[i] == 'S':
                    row[i] = 'O'