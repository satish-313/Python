class matrix:
    def __init__(self,row,col):
        self.row = row
        self.col = col
    def __str__(self):
        return f"{self.row} , {self.col}"

def main():
    lists = [1,2,3,4,5,6,7,8]
    number = 5
    m = []
    if number in lists:
        print("yes")
    for i in range(3):
        x = int(input("enter the row : "))
        y = int(input("Enter the col : "))
        z = matrix(x,y)
        m.append(z)
    
    for i in m:
        print(i)
    x = int(input("enter the row : "))
    y = int(input("Enter the col : "))
    z = matrix(x,y)

    if z in m:
        print(f" {z.row} and {z.col} in main list Yes")
    else:
        print(f" {z.row} and {z.col} in main list no ")

    
if __name__ == "__main__":
    main()