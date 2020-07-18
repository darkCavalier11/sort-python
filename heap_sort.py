def parent(i):
    return i//2
def left(i):
    return 2*i + 1
def right(i):
    return 2*i + 2

# max heapify take a single element and build heap

def max_heapify(A, i):
    l = left(i)
    r = right(i)
    if l < len(A) and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < len(A) and A[r] > A[largest]:
        largest = r
    if largest != i:
        temp = A[largest]
        A[largest] = A[i]
        A[i]= temp
        max_heapify(A, largest)
def build_max_heap(A):
    for i in range(len(A)//2, -1, -1):
        max_heapify(A, i)

array = [4,1,3,2,16,9,10,14,8,7]

def heap_sort(A):
    final = []
    build_max_heap(A)
    for i in range(len(A)-1, -1, -1):
        temp = A[i]
        A[i] = A[0]
        A[0] = temp
        final.append(A.pop())
        max_heapify(A, 0)
    return final
print(heap_sort(array))