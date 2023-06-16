def swap(array):
    for i in range (len(array)//2):
        temp=array[len(array)-1-i]
        array[len(array)-1-i]=array[i]
        array[i]=temp
    print(array)
swap([1,2,3,4,5])