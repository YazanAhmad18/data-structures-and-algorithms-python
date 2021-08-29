def insertion_sort(array_sort):
    i=1
    for i in range(len(array_sort)):
        j=i-1
        temporary=array_sort[i]
        while j>=0 and temporary < array_sort[j]:
            array_sort[j+1]=array_sort[j]
            j=j-1
            array_sort[j+1]= temporary
    return array_sort

if __name__=="__main__":
    print (insertion_sort([8,4,23,42,16,15]))
    print (insertion_sort([15,1,27,88,19,12]))