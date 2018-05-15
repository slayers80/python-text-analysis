# -*- coding: utf-8 -*-
"""
Created on Tue May 15 09:04:55 2018

@author: lwang
"""

def evalRPN(tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    ops = ['+','-','*','/']
    stack = []
    for op in tokens:            
        if op in ops:
            num2 = int(stack.pop())
            num1 = int(stack.pop())
            if op == '+':
                num = num1+num2
            if op == '-':
                num = num1-num2
            if op == '*':
                num = num1*num2
            if op == '/':                    
                num = int(num1/float(num2))
            stack.append(num)
        else:
            stack.append(int(op))
                 
    return stack[0]