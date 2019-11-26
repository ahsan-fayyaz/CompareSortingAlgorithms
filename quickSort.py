def quicksort(A, p, r):
    if(p < r):
        q = partition(A, p, r)
        quicksort(A, p, q)
        quicksort(A, q+1, r)
