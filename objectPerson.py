# for the object learing in python 

# for the create of class 
class person:
    def __init__(self , name , age): # for the initialize the data in person object instance
        self.name = name
        self.age = age
    def __str__(self):
        return f"Name : {self.name} \nage : {self.age}" # for string representation of object when it called

def main():
    name = input("Enter name : ")
    age = input("Enter age : ")
    p = person(name=name,age=age)
    print (p)
    name = input("want to change name : ")
    p.name = name
    print(p)


if __name__ == "__main__":
    main()