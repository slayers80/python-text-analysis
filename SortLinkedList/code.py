# -*- coding: utf-8 -*-
"""
Created on Sat May 12 18:30:01 2018

@author: lwang
"""

def sortList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not (head and head.next):
        return head
    
    dummy = ListNode(None)
    dummy.next = head
    fast = slow = dummy
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
        
    mid = slow.next
    slow.next = None
    
    h1 = self.sortList(head)
    h2 = self.sortList(mid)
            
    h = ListNode(None)
    res = h                   
    
    while h1 and h2:            
        if h1.val > h2.val:
            h.next = h2
            h = h2
            h2 = h2.next
        else:
            h.next = h1
            h = h1
            h1 = h1.next
    
    h.next = h1 or h2
    
    return res.next