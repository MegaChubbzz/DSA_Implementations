'''Implements stack and queue classes using a linked list'''

from Node import Node
from Linked_List_Class import LinkedList


class Stack:
    '''Stack class made using linked list'''
    def __init__(self):
        self.list = LinkedList()

    def push(self, new_item):
        '''Adds an item to the top of the stack'''
        new_node = Node(new_item)
        self.list.prepend(new_node)

    def pop(self):
        '''Remove and return the top item of the stack'''
        popped_item = self.list.head.data
        self.list.remove_after(None)
        return popped_item


class Queue:
    '''Queue class made using linked list'''
    def __init__(self):
        self.list = LinkedList()

    def enqueue(self, new_item):
        '''Add item to the back of the queue'''
        new_node = Node(new_item)
        self.list.append(new_node)

    def dequeue(self):
        '''Remove and return item at the front of the queue'''
        dequeued_item = self.list.head.data
        self.list.remove_after(None)
        return dequeued_item
