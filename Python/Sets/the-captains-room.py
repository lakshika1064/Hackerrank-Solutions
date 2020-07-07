# Enter your code here. Read input from STDIN. Print output to STDOUT
k=int(input())
l=list([int(i) for i in input().split()])
s=set(l)
print(((sum(s)*k)-(sum(l)))//(k-1))

'''
So in this we have k no. of groups and 1 captain 

Our list consist of every tourist room no. and all the members of a group stays in same room that means 
in our list list 1 room will occur k times

c is captains room number
g is group room number

Assume every room is occurring k times including captains room .
for this  ---> we will take a set and multiply its sum by k
equation 1 ==> (c + g)*k

now actual data 
equation 2 ==> c + g*k

subtract 
e1-e2= ck + gk - c -gk
e1-e2 = c(k-1)
c =  (e1-e2) // (k-1)
'''