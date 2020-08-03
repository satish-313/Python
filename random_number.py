import random

def main():
    n = int(input("enter number of element = "))
    letter = ['a','s','d','f']
    '''for i in range(n):
        l = input("enter the letter : ")
        letter.append(l)'''
    
    random_store = []
    for i in range(n*3):
        random_store.append(random.choice(letter))
    
    print(random_store)
    
    type_random = []
    print ("type the above sequence ")
    for i in range(n*3):
        mid = input()
        type_random.append(mid)
    
    print(type_random)

if __name__ == "__main__":
    main()