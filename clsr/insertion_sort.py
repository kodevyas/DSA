def main():
    num_list = [4,3,5,2,1,6]
    n = 6

    sorted_list = insertion_sort(num_list, n)

    print(sorted_list)


    
def insertion_sort(unsorted_list, n):
    for i in range(1,n):
        key = unsorted_list[i]
        j = i - 1
        while j >= 0 and unsorted_list[j] > key:
            unsorted_list[j+1] = unsorted_list[j]
            j = j - 1
        unsorted_list[j+1] = key
    return unsorted_list




if __name__ == "__main__":
    main()