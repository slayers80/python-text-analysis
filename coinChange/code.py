# -*- coding: utf-8 -*-
"""
Created on Fri May 18 12:51:06 2018

@author: lwang
"""

def coinChange(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    if not amount:
        return 0
    
    dp = [-1]*(amount+1)
    for n in range(amount+1):
        cand = []
        for coin in coins:
            if n>coin and dp[n-coin]!=-1:
                cand.append(dp[n-coin])
            elif n==coin:
                cand.append(0)
        if cand:
            dp[n] = 1+min(cand)
    #print dp
    return dp[-1]