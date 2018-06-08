# -*- coding: utf-8 -*-
"""
Created on Thu Jun 07 21:19:14 2018

@author: lwang
"""


def maxPathSum(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    
    maxsum = [-2**15+1]
    def postorder(node, maxsum):
        if node:                
    
            leftsum = postorder(node.left, maxsum)
            rightsum = postorder(node.right, maxsum)
            nodemax = node.val + max(0, leftsum, rightsum)
            
            maxsum[0] = max(maxsum[0], max(nodemax, node.val+leftsum+rightsum))      
            
            return nodemax
            
        else:
            return 0
    
    postorder(root, maxsum)
    
    return maxsum[0]