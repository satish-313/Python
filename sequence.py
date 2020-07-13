# different type of sequence like list, string, tuple, dictionary and set
string = input("Enter your name : ")

# for list
number_of_element = int(input("Enter the number of element is sequece : "))

_list = []
for i in range(number_of_element):
    x = int(input("enter the number : "))
    _list.append(x)

#the tuple
_tuple = (1, 2, 3,5,5,6)

print (f"the list are : \n {_list}")
print (f"the tuples are : \n {_tuple}")
print (f"string are also sequece data : {string}")