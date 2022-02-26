class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        # isnertar el valor al final de array, (append)
        self.heap.append(val)
        self.__percolateUp(len(self.heap) - 1)

    def get_max(self):
        if self.heap:
            return self.heap[0]
        return None

    def __swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def remove_max(self):
        if len(self.heap) > 1:
            max = self.heap[0]
            self.__swap(0, len(self.heap[0]) - 1)
            del self.heap[-1]
            self.__maxHeapify(0)
            return max

        # 1 element in the array
        elif self.heap[0]:
            max = self.heap[0]
            del self.heap[0]
            return max
        else:
            # no value in the array
            return None

    def __percolateUp(self, index):
        # reach first element
        parent = (index - 1) // 2
        if index <= 0:
            return

        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__percolateUp(parent)

    def __maxHeapify(self, index):

        left = (index * 2) + 1
        right = (index * 2) + 2
        largest = index

        if len(self.heap) > left and self.heap[left] > self.heap[largest]:
            largest = left
        if len(self.heap) > right and self.heap[right] > self.heap[largest]:
            largest = right

        #  if a found a largest value

        if largest != index:
            self.__swap(index, largest)
            self.__maxHeapify(largest)

    def build_heap(self, arr):
        self.heap = arr
        for value in arr:
            self.insert(value)


heap = MaxHeap()
heap = MaxHeap()
heap.insert(12)
heap.insert(10)
heap.insert(-10)
heap.insert(100)

print(heap.get_max())
