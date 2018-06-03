# -*- coding: utf-8 -*-
"""
Created on Sun Jun 03 14:45:13 2018

@author: lwang
"""

def getSkyline(buildings):
    """
    :type buildings: List[List[int]]
    :rtype: List[List[int]]
    """
    if buildings:
        res = []
        for i in range(len(buildings)):
            li, ri, hi = buildings[i]   
            keep_leftedge = True
            rightedge_maxh = 0
            rightedge_maxh_r = 0
            for j in range(len(buildings)):
                if i==j:
                    continue
                else:
                    lj, rj, hj = buildings[j]
                    
                    if lj<=li<=rj and hi<hj or lj<li<=rj and hi==hj:                            
                        keep_leftedge = False
                    if lj<=ri<rj and hj>rightedge_maxh:
                        rightedge_maxh = hj
                    
                        
            if keep_leftedge:
                if [li, hi] not in res:
                    res.append([li, hi])
            if rightedge_maxh<hi:
                if [ri, rightedge_maxh] not in res:
                    res.append([ri, rightedge_maxh])
        return sorted(res)
                
    return []    