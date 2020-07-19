def partition(A, p, r):
    x = A[r-1]
    i = p - 1
    for j in range(p, r-1):
        if A[j] <= x:
            i += 1
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
    temp = A[i+1]
    A[i+1] = A[r-1]
    A[r-1] = temp
    return i+1
def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)

