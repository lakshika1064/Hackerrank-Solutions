# Enter your code here. Read input from STDIN. Print output to STDOUT
rd,rm,ry=map(int,input().split())
ed,em,ey=map(int,input().split())
if ry<ey:
    print("0")
elif ry<=ey:
    if rm<=em:
        if rd<=ed:
            print("0")
        else:
            print(15*(rd-ed))
    else:
        print(500*(rm-em))
else:
    print(10000)


