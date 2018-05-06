# -*- coding: utf-8 -*-
"""
Created on Sun May 06 09:52:45 2018

@author: lwang
"""

def calculate(s):
    """
    :type s: str
    :rtype: int
    """
    
    if not s:
        return []
    
    stack = []
    
    ops = ['+','-','*','/']
    last_op = 0
    for i in range(len(s)):
        if s[i] in ops:
            num = int(s[last_op:i])
            last_op = i+1
            stack.append(num)
            stack.append(s[i])
        if i == len(s)-1:
            num = int(s[last_op:])
            stack.append(num)
    
    stack = stack[::-1]
    stack1 = []
    while stack:
        item = stack.pop()
        if item == '*':
            num1 = stack1.pop()
            num2 = stack.pop()
            stack1.append(num1*num2)
        elif item == '/':
            num1 = stack1.pop()
            num2 = stack.pop()
            stack1.append(num1/num2)
        else:
            stack1.append(item)
            
    stack1 = stack1[::-1]
    
    while stack1:
        item = stack1.pop()
        if item == '+':
            num2 = stack1.pop()
            num1 = num1+num2
        elif item == '-':
            num2 = stack1.pop()
            num1 = num1-num2
        else:
            num1 = item
            
    return num1


def calculate2(s):    
    """
    :type s: str
    :rtype: int
    """    
    if not s:
        return []
    
    ops = ['+','-','*','/']
    stack = []
    sign = '+'
    num = 0
    for i in range(len(s)):
        if s[i].isdigit():
            num = num*10 + ord(s[i]) - ord('0')
        if s[i] in ops or i==len(s)-1:
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack.append(num*stack.pop())
            elif sign == '/':
                num0 = stack.pop()
                if num0<0 and num0%num!=0:
                    stack.append(num0/num+1)
                else:
                    stack.append(num0/num)
            
            sign = s[i]
            num = 0
    
    return sum(stack)    