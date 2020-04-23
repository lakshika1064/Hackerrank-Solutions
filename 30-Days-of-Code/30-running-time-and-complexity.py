# Enter your code here. Read input from STDIN. Print output to STDOUT
T=int(input())
for t in range(T):
    n=int(input())
    if (n <= 1) : 
        print("Not prime")
    elif (n <= 3) : 
        print("Prime")
    elif (n % 2 == 0 or n % 3 == 0) : 
        print("Not prime")
    else:
        l=0
        i = 5
        while(i * i <= n) : 
            if (n % i == 0 or n % (i + 2) == 0) : 
                print("Not prime")
                l=1
                break
            i = i + 6
        if l==0:
            print("Prime")
      
        
