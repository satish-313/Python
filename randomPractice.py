import random

def repeatCheck(x,arr):
    t = True
    for i in arr:
        if i == x:
            t = False
            return t
    return t

def display(number):
    arr = []
    t = False
    while len(arr)!=number :
        #x = random.randrange(0,10,1)
        x = random.randint(0,10)
        t = repeatCheck(x,arr)
        if t :
            arr.append(x)
    return arr


def main():
    print("get a random number between 0 to 10")
    number = int(input("Enter the number of element : "))
    arr = display(number)
    print(arr)

if __name__ == "__main__":
    main()