# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 08:44:08 2018

@author: lwang
"""

def findWords(board, words):
    """
    :type board: List[List[str]]
    :type words: List[str]
    :rtype: List[str]
    """
    
    m, n = len(board), len(board[0])
    def search(i,j,m,n,newwords):
        if not words or i>=m or i<0 or j>=n or j<0:
            return False
        else:
            found = False
            nextwords = []
            for word in newwords:                    
                if board[i][j] == word[0]:
                    found = True
                    if word[1:]:
                        nextwords.append(word[1:])
            if found and nextwords:
                re = search(i-1,j,m,n,nextwords) or search(i+1,j,m,n,nextwords) or search(i,j-1,m,n,nextwords) or search(i,j+1,m,n,nextwords)
                if not re:
                    return False
                else:
                    return board[i][j]+re
            elif found and not nextwords:
                return board[i][j]
            else:
                return False
    
    res = []
    for i in range(m):
        for j in range(n):
            r = search(i,j,m,n,words)
            if r and r not in res:
                res.append(r)
                
    return res