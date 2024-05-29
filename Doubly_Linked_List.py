'''Linked list class for doubly-linked list'''


class LinkedList:
    '''Create Linked List instance, Node instances must be created and added to
    the list ex:  num_list = LinkedList() #creates empty linked list'''
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, new_node):
        '''Adds a node to the end of a linked list, making the node the tail,
        if linked list is empty it makes the new node the head and the tail
        of the linked list'''
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail  # Only for doubly-linked lists
            self.tail = new_node

    def prepend(self, new_node):
        '''Adds a node to the beginning of a linked list, making the node the
        head, if linked list is empty it makes the new node the head and the
        tail of the linked list'''
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node  # Only for doubly-linked lists
            self.head = new_node

    def insert_after(self, current_node, new_node):
        '''Inserts a node after an existing node'''
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif current_node is self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail  # Only for doubly-linked lists
            self.tail = new_node
        else:  # This else statement is only for doubly-linked lists
            successor_node = current_node.next
            new_node.next = successor_node
            new_node.prev = current_node
            current_node.next = new_node
            successor_node.prev = new_node

    def remove(self, current_node):  # Only for use with doubly-linked lists
        '''This method can only be used with doubly-linked lists, removes the
        specified node'''
        successor_node = current_node.next
        predecessor_node = current_node.prev
        if successor_node is not None:
            successor_node.prev = predecessor_node
        if predecessor_node is not None:
            predecessor_node.next = successor_node
        if current_node is self.head:
            self.head = successor_node
        if current_node is self.tail:
            self.tail = predecessor_node

    def insertion_sort_doubly_linked(self):
        '''Insertion sort algorithm that can only be used with doubly-linked
        list'''
        current_node = self.head.next
        while current_node is not None:
            next_node = current_node.next
            search_node = current_node.prev
            while ((search_node is not None) and (search_node.data > current_node.data)):
                search_node = search_node.prev
            self.remove(current_node)
            if search_node is None:
                current_node.prev = None
                self.prepend(current_node)
            else:
                self.insert_after(search_node, current_node)  # Be sure to use the correct else statement for doubly-linked lists
            current_node = next_node
