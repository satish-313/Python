# learing objects of more person 

class employes:
    def __init__(self, name, age ,wages):
        self.name = name
        self.age = age
        self.wages = wages
    
    def __str__(self):
        return f"name : {self.name}\nage : {self.age}\nwages : {self.wages}"
    
def printTheAll(listOfEmploye):
    for i in range(len(listOfEmploye)):
        print(listOfEmploye[i])

def changeApply(emp,change):
    if change == 1:
        name = input("Enter new name : ")
        emp.name = name
    elif change == 2:
        age = int(input("Enter the age : "))
        emp.age = age
    else :
        wages = float(input("Enter the wages :"))
        emp.wages = wages
    
    return emp

def update(listOfEmploye,wantToUpdate):
    if wantToUpdate == "yes":
        print ("who's want to change : enter the name ")
        printTheAll(listOfEmploye)
        name = input()
        for i in range(len(listOfEmploye)):
            if name == listOfEmploye[i].name:
                change = int(input("what want to change : name = 1 , age = 2 , wages = 3 : "))
                listOfEmploye[i] = changeApply(listOfEmploye[i],change)
        
        return listOfEmploye
    else:
        return listOfEmploye
        
def main():
    listOfEmploye = []
    numberOfEmploye = int(input("Enter the number of employes : "))
    for i in range(numberOfEmploye):
        name = input("Enter the employes name : ")
        age = int(input("Enter the employes age : "))
        wages = float(input("Enter the employes salary : "))
        p = employes(name = name, age = age ,wages = wages)
        listOfEmploye.append(p)

    printTheAll(listOfEmploye)

    wantToUpdate = input("For yes 'yes' no 'no' : ")
    listOfEmploye = update(listOfEmploye,wantToUpdate)
    printTheAll(listOfEmploye)

if __name__ == "__main__":
    main()

