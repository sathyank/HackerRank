#!/bin/python

import sys
def validate(inp):
    #if len(list(''.join(sorted(set(inp),key=inp.index))))==2:
    for i in range(len(inp)-1):
        if inp[i+1]==inp[i] :
            return False
    return True
    """else:
        return False"""

s_len = int(raw_input().strip())
s = raw_input().strip()

#tmp = list(set(s))
ans = 0

chDict = []
for ch in set(s):
    chDict.append((ch, len([j for j, x in enumerate(s) if x == ch])))

for i,t1 in enumerate(chDict[:-1]):
    ch_i, l_i = t1[0], t1[1]
    for j, t2 in enumerate(chDict[i+1:]):
        ch_j, l_j = t2[0], t2[1]
        if abs(l_i - l_j) < 2:
            c = [cha for cha in s if cha is ch_i or cha is ch_j]
            if validate(c):
                ans = max(ans,l_i+l_j)
            
print(ans)            