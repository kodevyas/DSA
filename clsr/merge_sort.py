
def merge_sort(unsorted_list, left_index, right_index):
    if right_index <= left_index:
        return 
    mid_index = (right_index + left_index)//2
    merge_sort(unsorted_list, left_index, mid_index)
    merge_sort(unsorted_list, mid_index + 1, right_index)
    merge(unsorted_list, left_index, mid_index, right_index)

    return unsorted_list



def merge(unsorted_list, left_index, mid_index, right_index):
    left_list = unsorted_list[left_index : mid_index + 1]
    right_list = unsorted_list[mid_index+1 : right_index + 1]
    

    i = left_index
    j, k = 0, 0
    while j < len(left_list) and k < len(right_list):
        if left_list[j] <= right_list[k]:
            unsorted_list[i] = left_list[j]
            j += 1
            i += 1
        else:
            unsorted_list[i] = right_list[k]
            k += 1
            i += 1
    if j < len(left_list):
        while j < len(left_list):
            unsorted_list[i] = left_list[j]
            i += 1
            j += 1
    elif k < len(right_list):
        while k < len(right_list):
            unsorted_list[i] = right_list[k]
            i += 1
            k += 1
    return unsorted_list