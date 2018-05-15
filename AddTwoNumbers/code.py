# -*- coding: utf-8 -*-
"""
Created on Mon May 14 21:16:02 2018

@author: lwang
"""

def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if not l1:
        return l2
    if not l2:
        return l1
    
    dummy = ListNode(None)
    carryover = 0
    lastnode = None
    while l1 and l2:
        s = l1.val+l2.val+carryover            
        node = ListNode(s%10)            
        carryover = s/10            
        if not lastnode:
            dummy.next = node
        else:
            lastnode.next = node            
        lastnode = node            
        l1 = l1.next
        l2 = l2.next
    
    if l1:
        while l1:
            s = l1.val+carryover
            node = ListNode(s%10)
            carryover = s/10                
            lastnode.next = node
            lastnode = node
            l1 = l1.next            
    
    if l2:
        while l2:
            s = l2.val+carryover
            node = ListNode(s%10)
            carryover = s/10                
            lastnode.next = node
            lastnode = node
            l2 = l2.next
            
    if not l1 and not l2 and carryover:
        node = ListNode(carryover)
        lastnode.next = node
            

    return dummy.next