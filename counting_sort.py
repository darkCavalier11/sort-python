def counting_sort(A):
    k = max(A)
    B = [0]*(len(A))
    C = [0]*(k+1)
    for m in range(len(A)):
        C[A[m]] = C[A[m]] + 1
    for i in range(1, k+1):
        C[i] = C[i] + C[i - 1]
    
    for j in range(len(A)-1, -1, -1):
        B[C[A[j]]-1] = A[j]
        C[A[j]] = C[A[j]] - 1
    return B
