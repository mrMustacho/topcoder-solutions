# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:01:38 2019

@author: Alejandro
"""

## Test Cases
test1 = ["-WW",
        "W-W",
        "WW-"]
test2 = ["-DD",
        "L-L",
        "WD-"]
test3 = ["-DWWD",
        "L-WLL",
        "DD-WD",
        "DDL-L",
        "DDLL-"]
test4 = ["-LWWLWDLDWWWWWWDDWDW",
        "D-WWLDDWDWDLWDDWLWDD",
        "LL-DLDWDLDLDWWWLWDDW",
        "LDD-LLLDLWLWWWWDWDWL",
        "LWWW-DWDLWDWDWWWDWDW",
        "DLLWD-WWLLDDDLWWDWWW",
        "WWLWDL-LLDWWWWWDWWLW",
        "LLLLLDW-LDLWDDLLLDWL",
        "DWWWWDDD-DWWWWDWWWDW",
        "WWWWLLLWL-LWWWWWLWWW",
        "DWWWWWWWLW-WDWWWWWWW",
        "DDDLLLDWWWL-DDWDWLDD",
        "LWLWLDLLLDLW-DDDWWDD",
        "LLWWLWDDLWLWL-WWWDLL",
        "WWWWLLDDDWLWDD-WWWLW",
        "DLDLLLWWLLLWWLW-DWLL",
        "DLWWWLDLWWDWWDWL-WWD",
        "LLDDLLWLLWLWLDLWW-WW",
        "LLWLLLWWLWLWWDWWLD-W",
        "LLWDLWDWDWLLWWDDWWL-"]

def points(matches):
    numberOfMatches = len(matches)
    pointsList = [0 for i in range(numberOfMatches)]
    for local in range(numberOfMatches):
        for visit in range(numberOfMatches):
            if matches[local][visit] == 'W':
                pointsList[local] += 3
            if matches[local][visit] == 'D':
                pointsList[local] += 1
                pointsList[visit] += 1
            if matches[local][visit] == 'L':
                pointsList[visit] += 3
    return pointsList

'''
## Prompt

print("Enter list of matches([W]in, [L], [D]raw or press Enter exit):")
matches = []
while True:
    buffer = input()
    if buffer == "":
        break
    matches.append(buffer)
'''

print(points(test1))
# Returns: {6, 6, 6 }
print(points(test2))
# Returns: {5, 2, 8 }
print(points(test3))
# Returns: {14, 7, 12, 8, 10 }
print(points(test4))
# Returns: {72, 62, 41, 41, 83, 63, 53, 35, 86, 50, 90, 32, 34, 41, 45, 36, 51, 32, 51, 45 }

'''
print("Matches: ")
print(matches)
print("Scores: ")
print(points(matches))
'''
