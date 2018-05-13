# -*- coding: utf-8 -*-
"""
Created on Sun May 13 10:17:12 2018

@author: lwang
"""

def lowestCommonAncestor(root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    path1 = []
    stack = []
    node = root
    done = False
    while not done:            
        if node:                
            if node == p:
                node2 = q
                done = True
            if node == q:
                node2 = p
                done = True
            stack.append(node)
            path1.append(node)
            node = node.left            
        else:
            if stack:
                node = stack.pop()                    
                if path1[-1] == node:                        
                    node = node.right
                else:
                    path1 = path1[:path1.index(node)+1]
                    node = node.right                    
            else:
                done = True
    
    #print path1[i].val
    
    path2 = []
    stack = []
    node = root
    done = False
    while not done:            
        if node:                
            if node == node2:                    
                done = True
            stack.append(node)
            path2.append(node)
            node = node.left            
        else:
            if stack:
                node = stack.pop()                    
                if path2[-1] == node:                        
                    node = node.right
                else:
                    path2 = path2[:path2.index(node)+1]
                    node = node.right                    
            else:
                done = True
    #print path2
    
           
    for i in range(min(len(path1), len(path2))):
        if path1[i] != path2[i]:
            return path1[i-1]
        
    return path1[i]