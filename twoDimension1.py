def main():
    diagonal = int(input("Enter the diagonal of matrix : "))
    arr = [0 for i in range(diagonal)]
    #arr = ['*' for i in range(diagonal)]
    print(arr)
    index = int(input("for modify the particular index : "))
    val = int(input("the value : "))
    #print(arr[index])
    arr[index] = val
    print(arr)
    arr2 = [[0 for i in range(diagonal)] for j in range(diagonal)]
    print(arr2)
    row = int(input("Enter the row : "))
    col = int(input("Enter the col : "))
    arr2[row][col] = val
    print(arr2)

if __name__ == "__main__":
    main()