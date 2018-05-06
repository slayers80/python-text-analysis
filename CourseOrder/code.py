# -*- coding: utf-8 -*-
"""
Created on Sun May 06 00:08:20 2018

@author: lwang
"""

def findOrder(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: List[int]
    """
    def dfs(node, graph):            
        if node in graph:
            for nextnode in graph[node]:
                if nextnode not in visited:
                    visited[nextnode] = True                        
                    visiting[nextnode] = True
                    if not dfs(nextnode, graph): 
                        return False
                    else:
                        visiting.pop(nextnode)
                        finished.append(nextnode)
                        print nextnode
                else:
                    if nextnode in visiting:
                        return False
        return True
    
    graph = {}
    for pair in prerequisites:
        if pair[1] not in graph:
            graph[pair[1]] = [pair[0]]
        else:
            graph[pair[1]].append(pair[0])
    
    visited = {}
    visiting = {}
    finished = []
    for i in range(numCourses):
        if i not in visited:
            visited[i] = True
            visiting[i] = True
            if not dfs(i, graph):
                return []
            else:
                visiting.pop(i)
                finished.append(i)
        else:
            if i in visiting:
                return []
                
    return finished[::-1]