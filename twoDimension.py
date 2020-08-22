def main():
    print("for the 1D array of using list : ")
    diagonal = int(input("Enter the diagonal of matrix : "))
    #arr1 = [0]*diagonal
    #print(arr1)
    #index1 = int(input("Enter the particular index : "))
    #print(arr1[index1])
    print("for the 2D array ")
    #row = int(input("Enter the row size : "))
    arr2 = [[0]*diagonal]*diagonal
    #print(arr2[index2row][index2col])
    #print(len(arr2))
    for i in range(len(arr2)):
        for j in range(len(arr2)):
            print(arr2[i][j],end=" ")
        print(" ")
    
    print ("For modify the index ")
    index2row = int(input("Enter the index of row "))
    index2col = int(input("Enter the index of col "))
    val = int(input("Enter the value : "))
    arr2[index2row][index2col] = val
    for i in range(len(arr2)):
        for j in range(len(arr2)):
            print(arr2[i][j],end=" ")
        print(" ")


if __name__ == "__main__":
    main()