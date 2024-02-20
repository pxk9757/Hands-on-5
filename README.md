# Create a MinHeap instance and build the heap
data = [4, 10, 3, 5, 1]
heap = MinHeap()
heap.build_min_heap(data)

# Display the initial Min Heap
print("Initial Min Heap:", heap.heap)
Output:
Initial Min Heap: [1, 4, 3, 10, 5]
Here, the initial Min Heap is built from the provided data [4, 10, 3, 5, 1].

# Push additional values onto the heap
heap.push(2)
heap.push(8)

# Display the Min Heap after pushing 2 and 8
print("Min Heap after pushing 2 and 8:", heap.heap)
Output:

Min Heap after pushing 2 and 8: [1, 2, 3, 10, 5, 8, 4]
After pushing the values 2 and 8 onto the heap, the heap property is maintained.

# Pop the root node and display the resulting heap
root = heap.pop()
print("Popped Root Node:", root)
print("Min Heap after popping root:", heap.heap)
Output:

Popped Root Node: 1
Min Heap after popping root: [2, 4, 3, 10, 5, 8]
After popping the root node (which is the minimum value in the heap), the heap is restructured to maintain the min heap property.

This demonstrates the functionality of building the initial heap, pushing values onto the heap, and popping the root node while maintaining the heap properties.

## Author-Priyanka Kondamadugu
