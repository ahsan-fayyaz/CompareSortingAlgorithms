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


#--------------DRIVER CODE------------------#

arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i]),
