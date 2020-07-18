# implementing priority queue on a heap
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

def heap_maximum(A):
    return A[0]

def heap_extract_max(A):
    if len(A) < 1:
        return "Heap Underflow"
    m = A[0]
    A[0] = A[len(A)-1]
    A.pop()
    max_heapify(A, 0)
    return m
def heap_increase_key(A, i, key):
    if key < A[i]:
        return 'new key smaller than current key'    
    A[i] = key
    while i > 0 and A[parent(i)] < A[i]:
        temp = A[i]
        A[i] = A[parent(i)]
        A[parent(i)] = temp
        i = parent(i)
        
def max_heap_insert(A, key):
    A.append(-float('inf'))
    heap_increase_key(A, len(A)-1, key)
