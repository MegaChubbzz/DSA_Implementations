'''Creating an array list class'''


class ArrayList:
    def __init__(self, initial_allocation_size=10):
        self.allocation_size = initial_allocation_size
        self.length = 0
        self.array = [None] * initial_allocation_size

    def append(self, new_item):
        if self.allocation_size == self.length:
            self.resize(self.length * 2)
        self.array[self.length] = new_item
        self.length = self.length + 1

    def resize(self, new_allocation_size):
        new_array = [None] * new_allocation_size
        for i in range(self.length):
            new_array[i] = self.array[i]
        self.array = new_array
        self.allocation_size = new_allocation_size

    def prepend(self, new_item):
        if self.allocation_size == self.length:
            self.resize(self.length * 2)
        for i in reversed(range(1, self.length + 1)):
            self.array[i] = self.array[i - 1]
        self.array[0] = new_item
        self.length = self.length + 1

    def insert_after(self, index, new_item):
        if self.allocation_size == self.length:
            self.resize(self.length * 2)
        for i in reversed(range(index + 1, self.length + 1)):
            self.array[i] = self.array[i - 1]
        self.array[index + 1] = new_item
        self.length = self.length + 1

    def search(self, item):
        for i in range(self.length):
            if self.array[i] == item:
                return i
        return -1

    def remove_at(self, index):
        if index >= 0 and index < self.length:
            for i in range(index, self.length - 1):
                self.array[i] = self.array[i + 1]
            self.length = self.length + 1


this = ArrayList(10)
for i in range(1, 6):
    this.append(i)
print(this.array)
