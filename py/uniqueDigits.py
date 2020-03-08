# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 16:17:41 2019

@author: Alejandro

"""
"""
for j in range(len(l)):
    if n[i] == l[j]:
        return False
    else:
        l.append(n[i])
"""
def compare(num):
    n = str(num)
    if num < 10:
        return True
    
    l = [n[0]]
    for i in range(1, len(n)):
        if n[i] in l:
            return False
        else:
            l.append(n[i])
    return True

      
def count(n):
    #vector = [1 for i in range(n)]
    cnt = 0
    for i in range(1, n):
        if compare(i):
            cnt += 1
    return cnt

n = int(input("Enter number:"))
print("Returns {}".format(count(n)))