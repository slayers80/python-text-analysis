# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 18:58:35 2018

@author: lwang
"""
#def strip_punc(s):
#    if s:
#        word = ''
#        for ch in s:
#            if ch.isalnum():                
#                word = word+ch
#        s = word
#    return s

file1 = open('file1.txt','r')
file2 = open('file2.txt','r')

file2_text = file2.read()

dic = {}
for word in file2_text.split():
    if word not in dic:
        dic[word.lower()] = 0

file1_text = file1.read()
for punc in '.,:;\'"!?-\n()[]{}%\\/':
    file1_text = file1_text.replace(punc, ' ')


for word in file1_text.split():
    word = word.lower()
    if word in dic:
        dic[word] += 1
    
output_str = ''        
for key in dic:
    print key, dic[key]
    output_str += ''.join([str(key),' ', str(dic[key]), '\n'])
    
file1.close()
file2.close()    

outputfile = open('output.txt','w')
outputfile.write(output_str)

outputfile.close()