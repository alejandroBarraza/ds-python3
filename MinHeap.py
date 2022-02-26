class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self.__precolate_up(len(self.heap) - 1)

    def get_min(self):
        if self.heap[0]:
            return self.heap[0]
        return None

    def remove_min(self):
        # case 1, at leat to element
        # case 2 , only one value in arr(heap)
        # case 2, arr(heap) is empty

        # case 1
        if len(self.heap) > 1:
            min = self.heap[0]
            self.__swap(0, len(self.heap) - 1)
            self.__min_hipify(0)
            del self.heap[-1]
            return min

        # case 2
        elif self.heap[0]:
            min = self.heap[0]
            del self.heap[0]
            return min
        # case 3
        else:
            return None

    def __swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def __precolate_up(self, index):
        parent = (index - 1) // 2

        # fist element(min),stop
        if index <= 0:
            return None

        elif self.heap[index] < self.heap[parent]:
            self.__swap(index, parent)
            self.__precolate_up(parent)

    def __min_hipify(self, index):
        left = (index * 2) + 1
        right = (index * 2) + 2
        smallest = index

        if len(self.heap) > left and self.heap[left] < self.heap[smallest]:
            smallest = left
        if len(self.heap) > right and self.heap[right] < self.heap[smallest]:
            smallest = right

        # found a min value
        if smallest != index:
            self.__swap(index, smallest)
            self.__min_hipify(smallest)


heap = MinHeap()
heap.insert(12)
heap.insert(10)
heap.insert(-10)
heap.insert(100)

print(heap.get_min())
print(heap.remove_min())
print(heap.get_min())
heap.insert(-100)
print(heap.get_min())
