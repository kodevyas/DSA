import insertion_sort
import reverse_insertion_sort
import merge_sort
import merge_sort_practise
def main():
    num_list = [4,3,5,2,1,6]
    new_num_list = num_list
    #num_list = [2,1]
    n = 6


    #### Insertion sort
    #sorted_list = insertion_sort.insertion_sort(num_list, n)
    #print(sorted_list)

    #### Reverse Insertion sort
    #reversed_sorted_list = reverse_insertion_sort.reverse_insertion_sort(num_list, n)
    #print(reversed_sorted_list)

    # Merge sort
    sorted_list = merge_sort.merge_sort(num_list, 0, 5) 
    print(sorted_list)


if __name__ == "__main__":
    main()