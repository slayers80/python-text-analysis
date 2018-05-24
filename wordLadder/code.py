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
    
def ladderLength2(beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: int
    """
    N = len(wordList)
    l = len(beginWord)
    if endWord not in set(wordList):
        return 0
    
    unvisited1 = set(wordList)
    unvisited2 = set(wordList)
    if beginWord in set(wordList):
        unvisited1.remove(beginWord)   
    else:
        unvisited2.add(beginWord)
        
    if endWord in unvisited2:
        unvisited2.remove(endWord)        
        
    frontiers1 = set([beginWord])
    frontiers2 = set([endWord])
    level1 = 1
    level2 = 1
    while frontiers1 and frontiers2:
        if len(frontiers1)<=len(frontiers2):
            nex1 = set()
            remainwords1 = set(unvisited1)
            for word1 in frontiers1:                              
                for word2 in unvisited1:        
                    if word2 in remainwords1:
                        counter = 0
                        for a, b in zip(word1, word2):
                            counter += a!=b
                            if counter == 2:
                                break
                        if counter == 1:
                            nex1.add(word2)                                                
                            remainwords1.remove(word2)

            frontiers1 = nex1
            unvisited1 = set(remainwords1)
            level1 += 1

            if set.intersection(frontiers1, frontiers2):                 
                return level1+level2-1
        else:
            nex2 = set()
            remainwords2 = set(unvisited2)
            for word1 in frontiers2:
                for word2 in unvisited2:
                    if word2 in remainwords2:
                        counter = 0
                        for a, b in zip(word1, word2):
                            counter += a!=b
                            if counter == 2:
                                break
                        if counter == 1:
                            nex2.add(word2)                                                
                            remainwords2.remove(word2)

            frontiers2 = nex2
            unvisited2 = set(remainwords2)
            level2 += 1

            if set.intersection(frontiers1, frontiers2):                 
                return level1+level2-1
        
    if endWord in unvisited1:
        return 0
    
def ladderLength3(beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: int
    """        
    l = len(beginWord)
    if endWord not in set(wordList):
        return 0
    
    unvisited1 = set(wordList)
    unvisited2 = set(wordList)
    if beginWord in set(wordList):
        unvisited1.remove(beginWord)   
    else:
        unvisited2.add(beginWord)
        
    if endWord in unvisited2:
        unvisited2.remove(endWord)        
        
    frontiers1 = set([beginWord])
    frontiers2 = set([endWord])
    level1 = 1
    level2 = 1
    while frontiers1 and frontiers2:
        if len(frontiers1)<=len(frontiers2):
            nex1 = set()
            remainwords1 = set(unvisited1)
            for word in frontiers1:
                for i in range(l):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        newword = word[:i]+c+word[i+1:]
                        if newword in unvisited1:                    
                            nex1.add(newword)                                                
                            remainwords1.remove(newword)  
                unvisited1 = set(remainwords1)
            frontiers1 = nex1                
            level1 += 1
        else:
            nex2 = set()
            remainwords2 = set(unvisited2)
            for word in frontiers2:
                for i in range(l):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        newword = word[:i]+c+word[i+1:]
                        if newword in unvisited2:                    
                            nex2.add(newword)                                                
                            remainwords2.remove(newword)  
                unvisited2 = set(remainwords2)
            frontiers2 = nex2                
            level2 += 1

        if set.intersection(frontiers1, frontiers2):
            return level1+level2-1
        
    if endWord in unvisited1:
        return 0
    
def ladderLength4(beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: int
    """        
    if endWord not in wordList:
        return 0
    length = 2
    front, back = set([beginWord]), set([endWord])
    wordList = set(wordList)
    
    wordList.discard(beginWord)
    while front:
        # generate all valid transformations
        front = wordList & (set(word[:index] + ch + word[index+1:] for word in front 
                            for index in range(len(beginWord)) for ch in 'abcdefghijklmnopqrstuvwxyz'))
        if front & back:
            # there are common elements in front and back, done
            return length
        length += 1
        if len(front) > len(back):
            # swap front and back for better performance (fewer choices in generating nextSet)
            front, back = back, front
        # remove transformations from wordDict to avoid cycle
        wordList -= front
    return 0    