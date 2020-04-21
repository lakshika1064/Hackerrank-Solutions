
#!/bin/python3
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []
    sum_list=[]
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    for i in range(0,4):
        for j in range(0,4):
            sum=0
            sum+=arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            sum_list.append(sum)
    print(max(sum_list))
        
