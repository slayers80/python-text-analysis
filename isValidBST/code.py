# -*- coding: utf-8 -*-
"""
Created on Sat May 19 22:29:44 2018

@author: lwang
"""

def isValidBST1(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    res = []
    def inordertraverse(root, res):
        if root:
            inordertraverse(root.left, res)
            res.append(root.val)
            inordertraverse(root.right, res)
    
    inordertraverse(root, res)
    
    if len(res)<=1:
        return True
    
    for i in range(1,len(res)):
        if res[i-1]>=res[i]:
            return False
    return True


def isValidBST2(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    res = []
    def inordertraverse(root, res):
        if root:
            if inordertraverse(root.left, res) == False:
                return False
            if not res or root.val>res[-1]:
                res.append(root.val)
            elif root.val<=res[-1]:
                return False                
            if inordertraverse(root.right, res) == False:
                return False
    
    if inordertraverse(root, res) == False:
        return False
    else:
        return True