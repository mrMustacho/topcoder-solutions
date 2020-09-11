# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 16:14:44 2019

@author: Alejandro
"""

def sponges(intensity, L, leftEnd, n, m):
    array = [[0 for j in range(n)] for i in range(m)]
    for i in range(m):
        for j in range(n):
            if leftEnd[i] + L-1>= j and leftEnd[i] <= j:
                array[i][j] = 1
    return array

def determineHumidity(intensity, L, leftEnd):
    n = len(intensity)
    m = len(leftEnd)
    drops = [0 for i in range(m)]
    s = sponges(intensity, L, leftEnd, n, m)
    for i in range(n):
        for j in range(m):
            if s[j][i] == 1:
                drops[j] += intensity[i]
                break
    return drops


print(determineHumidity(     
    [3, 4, 1, 1, 5, 6],
    3,
    [3, 1, 0]
    )
) # Returns: {12, 5, 3 }

print(determineHumidity(     
    [5, 5],
    2,
    [0, 0]
    )
)# Returns: {10, 0 }
print(determineHumidity(     
    [92, 11, 1000, 14, 3],
    2,
    [0, 3]
    )
)# Returns: {103, 17 }

print(determineHumidity(
    [2, 6, 15, 10, 8, 11, 99, 2, 4, 4, 4, 13], 
    4, 
    [1, 7, 4, 5, 8, 0]
    )
)# Returns: {39, 14, 110, 0, 13, 2 }