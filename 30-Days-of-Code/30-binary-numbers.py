#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    num=bin(n).replace("0b","") 
    res = [int(x) for x in str(num)] 
    count=[]
    t=0
    for i in res:
        if i==1:
            t+=1
        else: 
            count.append(t)
            t=0
    count.append(t)
    print(max(count))