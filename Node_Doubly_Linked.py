'''Node class for doubly-linked list'''


class Node:
    '''Create Node instance for node in linked list ex: node_a = Node(95)'''
    def __init__(self, initial_data):
        self.data = initial_data
        self.next = None
        self.prev = None  # Only for a doubly-linked list
