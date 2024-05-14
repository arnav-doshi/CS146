# Yes there is a way to use a max heap as a min heap, without recreating a whole extra implementation. Below is an implementation
# to create a max heap that retrieves the minimum values. This program does this by using a getMin() function that saves the minimum value
# of the heap by moving it to the root and performing heapifyDOWN operation to maintain the heap property.

# The opposite way is also possible, as it's possible to get the maximum from a minheap by extracting the root element, 
# which is the minimum value, then restoring the heap property through heapifyDown. 

def insert(heap, value):
    heap.append(value)
    heapifyUp(heap, len(heap) - 1)

def getMin(heap):
    if heap:
        min_value = heap[0]
        last_value = heap.pop()
        if heap:
            heap[0] = last_value
            heapifyDOWN(heap, 0)
        return min_value
    
    else:
        return None

def heapifyUp(heap, index):
    parent = (index - 1) // 2
    
    while index > 0 and heap[index] < heap[parent]:  
        heap[index], heap[parent] = heap[parent], heap[index]
        index = parent
        parent = (index - 1) // 2

def heapifyDOWN(heap, index):
    leftIndex = 2 * index + 1
    rightIndex = 2 * index + 2
    largest = index


    if leftIndex < len(heap) and heap[leftIndex] < heap[largest]:  
        largest = leftIndex
        
    if rightIndex < len(heap) and heap[rightIndex] < heap[largest]:
        largest = rightIndex
        
    if largest != index:
        heap[index], heap[largest] = heap[largest], heap[index]
        heapifyDOWN(heap, largest)

maxheap = []
insert(maxheap, 3)
insert(maxheap, 2)
insert(maxheap, 1)
insert(maxheap, 400)
insert(maxheap, 16)

print("Min values from max heap (in ascending order):")


while True:
    min = getMin(maxheap)
    if min is None:
        break
    print(min)
