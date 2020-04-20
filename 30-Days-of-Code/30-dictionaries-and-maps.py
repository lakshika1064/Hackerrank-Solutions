# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
dic={}
for i in range(0,n):
    name,phone = list(map(str , input().split()))
    dic[name]=phone
while(True):
        try:
            a=input()
            if a in dic:
                print(a+"="+dic[a])
            else:
                print("Not found")
        except Exception as e:
            break
        
