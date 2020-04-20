# Enter your code here. Read input from STDIN. Print output to STDOUT
T=int(input())
for i in range(0,T):
    S=input()
    e=""
    o=""
    for i in range(0,len(S)):
        if i%2==0:
            e+=S[i]
        else:
            o+=S[i]
    print(e+" "+o)