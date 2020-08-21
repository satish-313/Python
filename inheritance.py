class Person:
    def __init__(self,fName , lName):
        self.firstName = fName
        self.lastName = lName
    
    def printName(self):
        print(self.firstName ," ",self.lastName)
    
class Student(Person):
    def __init__(self,fName,lName,standard):
        #Person.__init__(self,fName,lName)
        super().__init__(fName,lName) # inherent all method of parent classs
        self.standard = standard #added another property
    def standardAttand(self):
        print("class attend is : ",self.standard)

def main():
    firstName = input("Enter your first name : ")
    lastName = input("Enter your last name : ")
    person = Person(firstName,lastName)
    person.printName()
    standard = int(input("Enter the class attend : "))
    student = Student(firstName,lastName,standard)
    student.printName()
    #print(student.standard)
    student.standardAttand()

if __name__ == "__main__":
    main()