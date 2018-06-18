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
                            res.add(branch+word[0])
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
    
    res = set()
    parents = set()
    branch=""
    remainingwords = set(words)
    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):
            remainingwords = remainingwords.difference(res)
            #print len(remainingwords),res
            if remainingwords:
                dfs(i,j,m,n,list(remainingwords),parents,branch,res)                
                
    return list(res)


def findWords2(board, words):
    
    def dfs(board, i, j, trie, partial):
        if '#' in trie:
            res.add(partial)
        if not (0 <= i < len(board)) or not (0 <= j < len(board[0])) or board[i][j] not in trie:
            return
        temp = board[i][j]
        board[i][j] = '@'
        [dfs(board, i+dx, j+dy, trie[temp], partial+temp) for dx, dy in directions]
        board[i][j] = temp
        
    trie, res = dict(), set()
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
    for word in words:
        t = trie
        for c in word:
            if c not in t:
                t[c] = dict()
            t = t[c]
        t['#'] = '#'
    for i in range(len(board)):
        for j in range(len(board[0])):
            dfs(board, i, j, trie, '')
    return res