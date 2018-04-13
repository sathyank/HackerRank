#!/bin/python

import sys

def check_beauty(s,k):
    for j in xrange(0,len(s)-k,k):
        if int(s[j+k:j+(2*k)])- int(s[j:j+k]) == 1:
            continue
        else:
            return False
    return True

q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    for i in xrange(1,(len(s)/2)+1,1):
        if(check_beauty(s,i)):
            print("YES "+s[0:i])
            break
    if i > len(s/2):
        print("NO")
