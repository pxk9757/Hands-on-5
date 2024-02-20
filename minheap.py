class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) >> 1

    def left(self, i):
        return (i << 1) + 1

    def right(self, i):
        return (i << 1) + 2

    def build_min_heap(self, data):
        self.heap = data[:]
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(i)

    def heapify(self, i):
        smallest = i
        l = self.left(i)
        r = self.right(i)

        if l < len(self.heap) and self.heap[l] < self.heap[smallest]:
            smallest = l

        if r < len(self.heap) and self.heap[r] < self.heap[smallest]:
            smallest = r

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(smallest)

    def push(self, value):
        self.heap.append(value)
        i = len(self.heap) - 1

        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def pop(self):
        if len(self.heap) == 0:
            return None

        root = self.heap[0]
        last_element = self.heap.pop()
        if len(self.heap) > 0:
            self.heap[0] = last_element
            self.heapify(0)

        return root


# Example usage:
# Create a min heap, build it, and demonstrate heap operations
data = [4, 10, 3, 5, 1]
heap = MinHeap()
heap.build_min_heap(data)

print("Initial Min Heap:", heap.heap)

# Push additional values
heap.push(2)
heap.push(8)
print("Min Heap after pushing 2 and 8:", heap.heap)

# Pop the root node
root = heap.pop()
print("Popped Root Node:", root)
print("Min Heap after popping root:", heap.heap)
