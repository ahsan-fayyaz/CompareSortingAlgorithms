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



#--------------DRIVER CODE------------------#


arr = [ 12, 11, 13, 5, 6, 7]
heapSort(arr)
n = len(arr)
print ("Sorted array is")
for i in range(n):
    print ("%d" %arr[i]),
