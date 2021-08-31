def  quick_sort(array, left_idx, right_idx):
    if left_idx < right_idx:
        position_idx = partition(array, left_idx, right_idx)
        quick_sort(array, left_idx, position_idx - 1)
        quick_sort(array, position_idx + 1, right_idx)
        return array




def partition(array, left_idx, right_idx):
    pivot_idx = array[right_idx]
    low = left_idx - 1
    for i in range(left_idx, right_idx ):
        if array[i] <= pivot_idx:
            low+=1
            Swap(array, i, low)
    Swap(array, right_idx, low + 1)
    return low+1




def Swap(array, i, low):
    temporary = array[i]
    array[i] = array[low]
    array[low] = temporary





if __name__=="__main__":
    smaple = [8,4,23,42,16,15]
    quick_sort(smaple, 0,len(smaple) - 1)
    print(f'quick Sorted array: {smaple}')