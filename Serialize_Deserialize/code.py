# -*- coding: utf-8 -*-
"""
Created on Tue May 29 23:13:40 2018

@author: lwang
"""

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def recur(node):
            if node:
                l.append(node.val)
                recur(node.left)
                recur(node.right)
            else:
                l.append(None)
        l = []
        recur(root)
        
        return l if l!=[None] else []

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def recur(data):
            
            if not data:
                return []
            
            node = TreeNode(None)
            if len(data)>=3:
                node.val = data.pop(0)
                
                if data[0]!=None:
                    node.left = recur(data)
                else:
                    node.left = data.pop(0)
                if data[0]!=None:
                    node.right = recur(data)
                else:
                    node.right = data.pop(0)
            
            return node
        
        return recur(data)