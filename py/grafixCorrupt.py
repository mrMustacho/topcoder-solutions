# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 16:41:51 2019

@author: Alejandro
"""

def selectWord(dictionary, candidate):
    n = len(dictionary)
    s = 0 #number of max similarities
    temp = 0 #temp. num. of similarities
    p = -1 #position of the similar word
    for i in range(n): #dictionary position
        for j in range(len(candidate)): 
            if candidate[j] == dictionary[i][j]:
                temp += 1
        if temp > s:
            s = temp
            p = i
        temp = 0
    return p

candidate = input("Enter candidate: ")
dictionary = []

print("Enter dictionary(press enter again to exit): ")
for i in range(50):
    buffer = input("[{}]: ".format(i))
    if buffer == "":
        break
    dictionary.append(buffer)

print("Candidate position: {}".format(selectWord(dictionary, candidate)))