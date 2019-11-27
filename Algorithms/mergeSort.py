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


#--------------DRIVER CODE------------------#
arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print ("Given array is")
for i in range(n):
    print ("%d" %arr[i]),

mergeSort(arr,0,n-1)
print ("\n\nSorted array is")
for i in range(n):
    print ("%d" %arr[i]),
