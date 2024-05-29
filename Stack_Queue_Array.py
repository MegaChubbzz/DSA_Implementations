'''Implenting a stack class using arrays'''


class StackUnbounded:
    '''This is how to easily implement a stack class using Python functions'''
    def __init__(self):
        self.stack_list = []

    def pop(self):
        '''Remove and return item from top of stack'''
        return self.stack_list.pop()

    def push(self, item):
        '''Add item to top of stack'''
        self.stack_list.append(item)


class Stack:
    '''This is how to implement a Python stack class that supports bounded or
    unbounded functionality'''
    def __init__(self, optional_max_length=-1):
        self.stack_list = []
        self.max_length = optional_max_length

    def pop(self):
        '''Remove and return item from top of stack'''
        return self.stack_list.pop()

    def push(self, item):
        '''Check to see if stack is full, if not full add item to top of stack,
        if full do not allow items to be added'''
        if len(self.stack_list) == self.max_length:
            return False
        self.stack_list.append(item)
        return True


class Queue:
    '''Implements a queue class using a list, can be either bounded or
    unbounded'''
    def __init__(self, optional_max_length=-1):
        self.queue_list = []
        self.front_index = 0
        self.length = 0
        self.max_length = optional_max_length

    def enqueue(self, item):
        '''Check to see if queue is full, if queue is not full add item to
        back of queue'''
        if self.length == self.max_length:
            return False
        if self.length == len(self.queue_list):
            self.resize()
        item_index = (self.front_index + self.length) % len(self.queue_list)
        self.queue_list[item_index] = item
        self.length += 1
        return True

    def dequeue(self):
        '''Remove and return item from front of queue'''
        to_return = self.queue_list[self.front_index]
        self.length -= 1
        self.front_index = (self.front_index + 1) % len(self.queue_list)
        return to_return

    def resize(self):
        '''Makes the list length larger if it is full as long as it does not
        exceed max length'''
        new_size = len(self.queue_list) * 2
        if self.max_length >= 0 and new_size > self.max_length:
            new_size = self.max_length
        new_list = [None] * new_size
        for i in range(self.length):
            item_index = (self.front_index + i) % len(self.queue_list)
            new_list[i] = self.queue_list[item_index]
        self.queue_list = new_list
        self.front_index = 0
