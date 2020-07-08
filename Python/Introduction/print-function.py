if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(i,end="")

'''
in this we have given both upper_limit and lower_limit to range function

print function by default put the end of line 
so to print in a single line we have used end="" that means to not take the cursor in the next line you can pass anything to the end function
example:
        end=";"  will work as  1;2;3;4......
'''