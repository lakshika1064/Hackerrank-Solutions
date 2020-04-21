class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self,firstName,lastName,ID,scores):
        Person.__init__(self,firstName,lastName,ID)
        self.scores=scores
    
    def calculate(self):
        S=0
        for i in range(0,len(scores)):
            S+=scores[i]
        S=S/len(scores)
        if S<=100 and S>=90:
            return "O"
        elif S>=80 and S<90:
            return "E"
        elif S>=70 and S<80:
            return "A"
        elif S>=55 and S<70:
            return "P"
        elif S>=40 and S<55:
            return "D"
        else:
            return "T"
        
    

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())