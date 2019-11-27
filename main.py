import math
from random import randint
import timeit


def welcome():
    str =  "    ------------------------------------\n"
    str += "    |      ALGORITHM RUN-TIME TOOL     |\n"
    str += "    ------------------------------------\n"
    str += "\n\n"
    str += "Welcome to the Algorithm run-time application\n"
    str += ".\n.\n.\n"
    str += "Please choose the Algorithm you wish to test\n"
    print(str)

def choose_algorithm():
    str =   "1)   Insertion Sort\n"
    str +=  "2)   Merge Sort\n"
    str +=  "3)   Heap Sort\n"
    str +=  "4)   Quick Sort\n"
    #str +=  "5)   Quick Sort (Random Pivot)\n"
    print(str)

def user_input():
    user_input = int(input("Select the appropriate number: "))
    return user_input

def choose_input_size():
    n = int(input("Please choose the array size: "))
    return n


def generate_random_array_of_size(n):
    Array = [0] * n
    for i in range(0,n):
        x = randint(0,n)
        Array[i] = x
    return Array

def sort(array, algorithm):
    n = len(array)
    if (algorithm == 1):
        start = timeit.default_timer()
        array = insertionSort(array, n)
        stop = timeit.default_timer()
        time = stop - start
        return array, time

    elif (algorithm == 2):
        start = timeit.default_timer()
        mergeSort(array, 0, n-1)
        stop = timeit.default_timer()
        time = stop - start
        return array, time

    elif (algorithm == 3):
        start = timeit.default_timer()
        heapSort(array)
        stop = timeit.default_timer()
        time = stop - start
        return array, time

    elif(algorithm == 4):
        start = timeit.default_timer()
        quickSort(array, 0, n-1)
        stop = timeit.default_timer()
        time = stop - start
        return array, time




#------------------Insertion Sort------------------#
def insertionSort(array, n):
    num = 1
    for j in range(1, n):
        key = array[j]
        i = j - 1
        while (i>=0 and array[i]>key):
            array[i+1] = array[i]
            i-=1
        array[i+1] = key

        num += 1
    return array


#------------------Merge Sort------------------#
import math
def mergeSort(A, left, right):
    if (left < right):
        mid = math.floor((left + right) / 2)

        mergeSort(A, left, mid)
        mergeSort(A, mid + 1, right)
        merge(A, left, mid, right)




def merge(A, low, mid, high):
    n1 = mid - low + 1
    n2 = high - mid

    left_subArray = [0] * (n1)
    right_subArray = [0] * (n2)

    for i in range(0, n1):
        left_subArray[i] = A[low + i]

    for j in range(0, n2):
        right_subArray[j] = A[mid + j + 1]

    i = 0;
    j = 0
    k = low

    while (i < n1 and j < n2):
        if left_subArray[i] <= right_subArray[j]:
            A[k] = left_subArray[i]
            i=i+1
        else:
            A[k] = right_subArray[j]
            j=j+1
        k += 1

    while (i < n1):
        A[k] = left_subArray[i]
        i += 1
        k += 1


#------------------Heap Sort------------------#
def heapify(A, n, i):
    left = 2*i + 1
    right = 2*i + 2

    if ((left < n) and (A[left] > A[i])):
        largest = left
    else:
        largest = i

    if ((right < n) and (A[right] > A[largest])):
        largest = right

    if (largest != i):
        A[i], A[largest] = A[largest], A[i]
        heapify(A, n, largest)


def heapSort(A):
    n = len(A)

    for i in range(n, -1, -1):
        heapify(A, n, i)

    for i in range(n-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapify(A, i, 0)


#------------------Quick Sort------------------#
def quickSort(A, low, high):
    if(low < high):
        partition_index = partition(A, low, high)
        quickSort(A, low, partition_index-1)
        quickSort(A, partition_index+1, high)

def partition(A, low, high):
    pivot = A[high]
    i = low - 1

    for j in range(low, high):
        if A[j] <= pivot:
            i = i + 1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[high] = A[high], A[i+1]

    return (i+1)


def print_which_algorithm_user_chose(algorithm_number, input_size_of_array):
    size = str(input_size_of_array)
    str_output = "\n\n#---------You have chosen "
    if algorithm_number == 1:
        str_output += "INSERTION SORT"
    if algorithm_number == 2:
        str_output += "MERGE SORT"
    if algorithm_number == 3:
        str_output += "HEAP SORT"
    if algorithm_number == 4:
        str_output += "QUICK SORT"
    if algorithm_number == 5:
        str_output += "QUICK SORT (Random Pivot)"
    str_output += "---------#\n"
    str_output += ""
    str_output += "Array Size = " + size
    str_output += "\n\n"
    print(str_output)

def round_to_n_significant(time):
    n = 3
    return round(time, n)

def convert_s_to_ms(time):
    return time * 1000

def want_to_print():
    str_input = str(input("Do you want to print the arrays? "))
    print = False
    if ((str_input == "Y") or (str_input == 'y') or \
        (str_input == "Yes") or (str_input == 'yes')):
        print = True
    else:
        print = False
    return print

def print_unsorted_and_sorted_arrays(unsorted, sorted):
    print("Unsorted Random Array: ", end="")
    print("[",end=" ")
    for item in array:
        print(str(item), end= " ")
    print("]\n")

    print("Sorted Array: ", end="")
    print("[",end=" ")
    for item in sorted_array:
        print(str(item),end=" ")
    print("]\n")



#----------------------------------------main run function--------------------------------#
def main_run():
    welcome()
    choose_algorithm()
    algorithm_chosen = user_input()
    n =  choose_input_size()
    print_choice = False
    if(n <= 100):
        print_choice = want_to_print()
    print_which_algorithm_user_chose(algorithm_chosen, n)
    array = generate_random_array_of_size(n)
    print("Sorting...\n\n")
    sorted_array, time = sort(array, algorithm_chosen)
    time_in_millisecond = convert_s_to_ms(time)
    time_in_n_sf = round_to_n_significant(time_in_millisecond)

    if(print_choice):
        print_unsorted_and_sorted_arrays(array, sorted_array)

    print("Total time taken: ", time_in_n_sf, " milliseconds")




if __name__ == '__main__':
    main_run()
