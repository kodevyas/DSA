import insertion_sort
import reverse_insertion_sort

def main():
    num_list = [4,3,5,2,1,6]
    n = 6


    # Insertion sort
    sorted_list = insertion_sort.insertion_sort(num_list, n)
    print(sorted_list)

    # Reverse Insertion sort
    reversed_sorted_list = reverse_insertion_sort.reverse_insertion_sort(num_list, n)
    print(reversed_sorted_list)


if __name__ == "__main__":
    main()