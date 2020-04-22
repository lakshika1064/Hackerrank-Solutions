#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
swa = 0
for i in range(n):
    for j in range(i+1,n):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
            swa+= 1
print("Array is sorted in "+str(swa)+" swaps.")
print("First Element: "+str(a[0]))
print("Last Element: "+str(a[n-1]))
