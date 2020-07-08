if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)

'''
/ ---->  floating point division 
it will return you the float value
example:  
        4/2 = 2.0
        3/2 = 1.5
        -3/2 = -1.5
        4.0/2 = 2.0

// -----> floor division or integer division
in this if the result is positive than the digits after decimal is simply removed
else if one of the operand is negative than the result is floored that means towards negative infinity example
(-1.2 ,3.4) = (-2 ,3)
example:
        4//2 = 2
        3//2 = 1
        -3 // 2 =-2
        4.0//2 = 2.0
'''