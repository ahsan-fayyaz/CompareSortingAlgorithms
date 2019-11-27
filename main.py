from insertionSort import insertionSort
from mergeSort import mergeSort
from heapSort import heapSort
from quickSort import quickSort


def main_run():
    welcome()
    choose_algorithm()
    algorithm_chosen = user_input()
    n =  choose_input_size()
    array = generate_random_array_of_size(n)

    sort(array, algorithm_chosen)

def welcome():
    str = "Welcome to the Algorithm run-time checking application\n"
    str += ".\n.\n.\n.\n.\n.\n"
    str += "Please choose the Algorithm you wish to test\n"
    print(str)

def choose_algorithm():
    str =   "1)   Insertion Sort\n"
    str +=  "2)   Merge Sort\n"
    str +=  "3)   Heap Sort\n"
    str +=  "4)   Quick Sort\n"
    str +=  "5)   Quick Sort (Random Pivot)\n"
    print(str)

def user_input():
    input = int(input("Select the appropriate number"))
    return input

def choose_input_size():
    n = int(input("Please choose the array size: "))
    return n


def generate_random_array_of_size(n)
    Array = [0] * n
    print(Array)
    for i in range(0,n):
        x = randint(0,n)
        Array[i] = x
    return Array

def sort(array, algorithm):
    sorted_array = []
    if (algorithm == 1):
        #insertion sort

    elif (algorithm == 2):
        #merge sort

    elif (algorithm == 3):
        #heapSort

    elif(algorithm == 4):
        #quicksort
