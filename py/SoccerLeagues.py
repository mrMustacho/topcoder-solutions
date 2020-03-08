# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:01:38 2019

@author: Alejandro
"""

def points(matches):
    n = len(matches)
    plist = [0 for i in range(n)]
    for local in range(n):
        for visit in range(n):
            if matches[local][visit] == 'W':
                plist[local] += 3
            if matches[local][visit] == 'D':
                plist[local] += 1
                plist[visit] += 1
            if matches[local][visit] == 'L':
                plist[visit] += 3
    return plist

print("Enter list of matches(press enter again to exit):")
matches = []
while True:
    buffer = input()
    if buffer == "":
        break
    matches.append(buffer)

print("Matches: ")
print(matches)
print("Scores: ")
print(points(matches))
