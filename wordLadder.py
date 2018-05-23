# -*- coding: utf-8 -*-
"""
Created on Wed May 23 08:26:16 2018

@author: lwang
"""

def ladderLength(beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: int
    """
    N = len(wordList)
    l = len(beginWord)
    if endWord not in wordList:
        return 0
    
    unvisited = wordList[:]
    if beginWord in unvisited:
        unvisited.remove(beginWord)        
    
    frontiers = [beginWord]
    level = 1        
    while frontiers:
        nex = set()
        remainwords = set(unvisited)
        for word1 in frontiers:
            if word1 == endWord:                    
                return level                 
            for word2 in unvisited:        
                if word2 in remainwords:
                    counter = 0
                    for a, b in zip(word1, word2):
                        counter += a!=b
                        if counter == 2:
                            break
                    if counter == 1:
                        nex.add(word2)                    
                        if word2 in remainwords:
                            remainwords.remove(word2)
                    
        frontiers = list(nex)
        unvisited = list(remainwords)
        level += 1
        print len(nex), len(remainwords)
        
    if endWord in unvisited:
        return 0