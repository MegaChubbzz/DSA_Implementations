'''Implementation of max heap data structure'''

class MaxHeap:
    def __init__(self):
        self.heap_array = []

    def percolate_up(self, node_index):
        while node_index > 0:
            parent_index = (node_index - 1) // 2
            if self.heap_array[node_index] <= self.heap_array[parent_index]:
                return
            else:
                temp = self.heap_array[node_index]
                self.heap_array[node_index] = self.heap_array[parent_index]
                self.heap_array[parent_index] = temp
                node_index = parent_index

    def percolate_down(self, node_index):
        child_index = 2 * node_index + 1
        value = self.heap_array[node_index]
        while child_index < len(self.heap_array):
            max_value = value
            max_index = -1
            i = 0
            while i < 2 and i + child_index < len(self.heap_array):
                if self.heap_array[i + child_index] > max_value:
                    max_value = self.heap_array[i + child_index]
                    max_index = i + child_index
                i = i + 1
            if max_value == value:
                return
            else:
                temp = self.heap_array[node_index]
                self.heap_array[node_index] = self.heap_array[max_index]
                self.heap_array[max_index] = temp
                node_index = max_index
                child_index = 2 * node_index + 1

    def insert(self, value):
        self.heap_array.append(value)
        self.percolate_up(len(self.heap_array) - 1)

    def remove(self):
        max_value = self.heap_array[0]
        replace_value = self.heap_array.pop()
        if len(self.heap_array) > 0:
            self.heap_array[0] = replace_value
            self.percolate_down(0)
        return max_value
    
def max_heap_percolate_down(node_index, heap_list, list_size):
    child_index = 2 * node_index + 1
    value = heap_list[node_index]
    while child_index < list_size:
        max_value = value
        max_index = -1
        i = 0
        while i < 2 and i + child_index < list_size:
            if heap_list[i + child_index] > max_value:
                max_value = heap_list[i + child_index]
                max_index = i + child_index
            i = i + 1
        if max_value == value:
            return
        temp = heap_list[node_index]
        heap_list[node_index] = heap_list[max_index]
        heap_list[max_index] = temp
        node_index = max_index
        child_index = 2 * node_index + 1

def heap_sort(numbers):
    i = len(numbers) // 2 - 1
    while i >= 0:
        max_heap_percolate_down(i, numbers, len(numbers))
        i = i - 1
    i = len(numbers) - 1
    while i >= 0:
        temp = numbers[0]
        numbers[0] = numbers[i]
        numbers[i] = temp
        max_heap_percolate_down(0, numbers, i)
        i = i - 1


numbers_list = [19, 87, 33, 22, 61, 12]
heap_sort(numbers_list)
print(numbers_list)
