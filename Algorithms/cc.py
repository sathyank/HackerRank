#!/bin/python

import sys


n = int(raw_input().strip())
s = raw_input().strip()
k = int(raw_input().strip())
s = list(s)
for i in range(n):
    #if s[i].isalpha():
    if (ord(s[i]) >= 97) and (ord(s[i]) <= 122):
        if (ord(s[i]) + k) >= 97 and (ord(s[i]) + k) < 122:
            s[i] = chr(ord(s[i]) + k)
        elif (ord(s[i]) + k)> 122:
            tmp = (ord(s[i])+k) - 122
            s[i] = chr(ord("a") + tmp-1)
    elif (ord(s[i]) >= 65) and (ord(s[i]) <= 90): 
        if (ord(s[i]) + k) >= 65 and (ord(s[i]) + k) < 90:
            s[i] = chr(ord(s[i]) + k)
        elif (ord(s[i]) + k) > 90:
            tmp = (ord(s[i])+k) - 90
            s[i] = chr(ord("A") + tmp-1)  

                
print("".join(s))                