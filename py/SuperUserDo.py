# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:36:09 2019

@author: Alejandro
"""

def install(A, B):
    n = len(A)
    buffer = [0 for i in range(1001)]
    for i in range(n):
        for j in range(A[i], B[i]+1):
            buffer[j] = 1
    return sum(buffer)

A = []
B = []
buffer = 0
print("Enter A and B list(press 0 in A tu break):")
for i in range(1001):
    buffer = int(input("A[{}]:".format(i)))
    if buffer == 0:
        break
    A.append(buffer)
    buffer = int(input("B[{}]:".format(i)))
    B.append(buffer)

print("num. of libraries: {}".format(install(A, B)))