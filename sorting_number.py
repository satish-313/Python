# sorting of number
class index :
    def __init__(self,xstream,indexs):
        self.xstream = xstream
        self.indexs = indexs
    
def min(lists):
    mx = lists[0]
    mi =0
    for i,s  in enumerate(lists):
        if mx > s :
            mx = s
            mi= i

    mins = index(mx,mi)
    return mins
    
def max (lists):
    mx = lists[0]
    mi = 0
    for i,s in enumerate(lists):
        if mx < s:
            mx = s
            mi = i

    maxs = index(mx,mi)
    return maxs

def sort (tye,lists):
    sorted_list = []    
    if tye == 1:
        while len(lists) != 0:
            lo = min(lists)
            sorted_list.append(lo.xstream)
            lists.pop(lo.indexs)

        return sorted_list
    else:
        while len(lists) != 0:
            la = max(lists)
            sorted_list.append(la.xstream)
            lists.pop(la.indexs)

        return sorted_list



def main ():
    name_ = input("Enter your name : ")
    numbers = int(input(f"Hi {name_} enter number of elements : "))
    unsorted_list = []
    for i in range(numbers):
        x = int(input("Enter the number : " ))
        unsorted_list.append(x)
    
    tye = int(input("for asc 1 and for des anyother: "))

    sorted_list = sort(tye,unsorted_list)
    print (f"The sored list is :\n{sorted_list} ")


if __name__ == "__main__":
    main()