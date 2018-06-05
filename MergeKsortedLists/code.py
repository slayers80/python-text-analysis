# -*- coding: utf-8 -*-
"""
Created on Tue Jun 05 09:28:20 2018

@author: lwang
"""

from heapq import *
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        l = len(lists)
        if not l:
            return None
        
        dummy = ListNode(None)
        head = dummy
        heap = []
        heapify(heap)
        done = [True]*l
        
        for i in range(l):
            if lists[i]:
                heappush(heap, (lists[i].val, i))
            elif done[i]:
                done[i] = False
                
        while True:
            if any(done):
                minval , whichlist = heappop(heap)
                
                head.next = lists[whichlist]
                head = head.next
                lists[whichlist] = lists[whichlist].next
                if lists[whichlist]:
                    heappush(heap, (lists[whichlist].val, whichlist))
                else:
                    done[whichlist] = False
            else:
                break
        return dummy.next