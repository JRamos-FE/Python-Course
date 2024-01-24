import heapq

# Create an empty heap
heap = []

# Add some elements to the heap
heapq.heappush(heap, 10)
heapq.heappush(heap, 5)
heapq.heappush(heap, 20)

# Pop and return the smallest item from the heap
smallest = heapq.heappop(heap)
print(smallest)  # Output: 5

# The remaining heap
print(heap)  # Output: [10, 20]

# Heapify method
L = [50, 30, 60, 40, 70, 20, 10]
heapq.heapify(L)
print(L)

# Heap n largest
print(heapq.nlargest(2, L))

# Heap n smallest
print(heapq.nsmallest(3, L))

