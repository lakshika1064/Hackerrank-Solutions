class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference=0
    # Add your code here
    def computeDifference(self):
        dif=list()
        for i in range(0,len(a)-1):
            for j in range(i+1,len(a)):
                dif.append(abs(a[i]-a[j]))
        self.maximumDifference=max(dif)
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)