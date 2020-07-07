t=int(input())
while t>0:
    an , a , bn , b = int(input()) , set(input().split()) , int(input()) , set(input().split())
    print(a.issubset(b))
    t=t-1