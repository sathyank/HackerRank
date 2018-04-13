#!/bin/python
import re
import sys

alpha = list("abcdefghijklmnopqrstuvwxyz")

def gemstones(arr):
    count = 0
    times = 0
    for tmp in alpha:
        for string in arr:
            if re.search(tmp,string):
                times +=1
                continue
            else:
                break
        if times == len(arr):
            count+=1
    return count        

n = int(raw_input().strip())
arr = []
arr_i = 0
for arr_i in xrange(n):
    arr_t = str(raw_input().strip())
    arr.append(arr_t)
result = gemstones(arr)
print(result)
