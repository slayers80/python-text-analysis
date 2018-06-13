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
    def dfs(i,j,m,n,newwords,parents,branch,res):
        
        if (i,j) not in parents:
            nextwords = []
            for word in newwords:
                if board[i][j] == word[0]:
                    if word[1:]:
                        nextwords.append(word[1:])                            
                    else:
                        if branch+word[0] not in res:
                            res.append(branch+word[0])
            #print (i,j), branch, parents, nextwords
            if nextwords:                    
                if i-1>=0:
                    branch = branch+board[i][j]
                    parents.add((i,j))
                    dfs(i-1,j,m,n,nextwords,parents,branch,res)
                    branch = branch[:-1]
                    parents.remove((i,j))
                if i+1<m:
                    branch = branch+board[i][j]
                    parents.add((i,j))
                    dfs(i+1,j,m,n,nextwords,parents,branch,res)
                    branch = branch[:-1]
                    parents.remove((i,j))
                if j-1>=0:
                    branch = branch+board[i][j]
                    parents.add((i,j))
                    dfs(i,j-1,m,n,nextwords,parents,branch,res)
                    branch = branch[:-1]
                    parents.remove((i,j))
                if j+1<n:
                    branch = branch+board[i][j]
                    parents.add((i,j))
                    dfs(i,j+1,m,n,nextwords,parents,branch,res)
                    branch = branch[:-1]
                    parents.remove((i,j))
    
    res = []
    parents = set()
    branch=""
    for i in range(m):
        for j in range(n):
            dfs(i,j,m,n,words,parents,branch,res)                
               
    return res