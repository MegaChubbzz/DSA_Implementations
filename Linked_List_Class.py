''' Linked list class for singly-linked list'''


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
            self.head = new_node

    def insert_after(self, current_node, new_node):
        '''Inserts a node after an existing node'''
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif current_node is self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            new_node.next = current_node.next
            current_node.next = new_node

    def remove_after(self, current_node):
        '''Removes a node after the specified node'''
        # Special case, remove head
        if (current_node is None) and (self.head is not None):
            succeeding_node = self.head.next
            self.head = succeeding_node
            if succeeding_node is None:  # Remove last item
                self.tail = None
        elif current_node.next is not None:
            succeeding_node = current_node.next.next
            current_node.next = succeeding_node
            if succeeding_node is None:  # Remove tail
                self.tail = current_node

    def insertion_sort_singly_linked(self):
        '''Insert sort method for singly linked lists, uses the
        find_insertion_position method'''
        before_current = self.head
        current_node = self.head.next
        while current_node is not None:
            next_node = current_node.next
            position = self.find_insertion_position(current_node.data)
            if position == before_current:
                before_current = current_node
            else:
                self.remove_after(before_current)
                if position is None:
                    self.prepend(current_node)
                else:
                    self.insert_after(position, current_node)
            current_node = next_node

    def find_insertion_position(self, data_value):
        '''Method used with insertion_sort_singly_linked to find the correct
        insertion position of the node'''
        position_a = None
        position_b = self.head
        while (position_b is not None) and (data_value > position_b.data):
            position_a = position_b
            position_b = position_b.next
        return position_a
