def merge_sort(array):
    if len(array)>1:
        middle_of_array=len(array)//2
        left_side=array[:middle_of_array]
        right_side=array[middle_of_array:]
        merge_sort(left_side)
        merge_sort(right_side)
        merge(left_side,right_side,array)
    return(array)    
      

def merge(left_side,right_side,array):
    i_left_side=0
    j_right_side=0
    array_index=0
    while i_left_side<len(left_side) and j_right_side<len(right_side):
        if left_side[i_left_side] <= right_side[j_right_side]:
            array[array_index]=left_side[i_left_side]
            i_left_side =i_left_side+1
        else:
            array[array_index]=right_side[j_right_side]
            j_right_side =j_right_side+1
        array_index=array_index+1

    
    while i_left_side < len(left_side):
        array[array_index] = left_side[i_left_side]
        i_left_side =i_left_side + 1
        array_index =array_index+ 1

    while j_right_side < len(right_side):
        array[array_index] = right_side[j_right_side]
        j_right_side=j_right_side+ 1
        array_index = array_index+1


if __name__=="__main__":
   print (merge_sort([8,4,23,42,16,15]))