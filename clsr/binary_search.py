def binary_search(num_list, l, r, x):
    while l < r :
        mid = (l + r) // 2
        if num_list[mid] == x :
            return mid
        elif num_list[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1 
    