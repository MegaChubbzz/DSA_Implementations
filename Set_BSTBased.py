'''Set implementation using a binary search tree'''

class BSTNode:
    def __init__(self, data, parent, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def count(self):
        leftCount = 0
        rightCount = 0
        if self.left != None:
            leftCount = self.left.count()
        if self.right != None:
            rightCount = self.right.count()
        return 1 + leftCount + rightCount
    
    def get_successor(self):
        if self.right != None:
            successor = self.right
            while successor.left != None:
                successor = successor.left
            return successor
        node = self
        while node.parent != None and node == node.parent.right:
            node = node.parent
        return node.parent
    
    def replace_child(self, current_child, new_child):
        if current_child is self.left:
            self.left = new_child
            if self.left:
                self.left.parent = self
        elif current_child is self.right:
            self.right = new_child
            if self.right:
                self.right.parent = self


class BSTIterator:
    def __init__(self, node):
        self.node = node

    def __next__(self):
        return self.next()
    

class Set:
    def __init__(self, get_key_function=None):
        self.storage_root = None
        if get_key_function == None:
            self.get_key = lambda el: el
        else:
            self.get_key = get_key_function

    def __iter__(self):
        if self.storage_root == None:
            return BSTIterator(None)
        minNode = self.storage_root
        while minNode.left != None:
            minNode = minNode.left
        return BSTIterator(minNode)
    
    def add(self, new_element):
        new_elementKey = self.get_key(new_element)
        if self.node_search(new_elementKey) != None:
            return False
        newNode = BSTNode(new_element, None)
        if self.storage_root == None:
            self.storage_root = newNode
        else:
            node = self.storage_root
            while node != None:
                if new_elementKey < self.get_key(node.data):
                    if node.left:
                        node = node.left
                    else:
                        node.left = newNode
                        newNode.parent = node
                        return True
                else:
                    if node.right:
                        node = node.right
                    else:
                        node.right = newNode
                        newNode.parent = node
                        return True
    
    def difference(self, other_set):
        result = Set(self.get_key)
        for element in self:
            if other_set.search(self.get_key(element)) == None:
                result.add(element)
        return result
    
    def filter(self, predicate):
        result = Set(self.get_key)
        for element in self:
            if predicate(element):
                result.add(element)
        return result
    
    def intersection(self, other_set):
        result = Set(self.get_key)
        for element in self:
            if other_set.search(self.get_key(element)) != None:
                result.add(element)
        return result
    
    def __len__(self):
        if self.storage_root == None:
            return 0
        return self.storage_root.count()
    
    def map(self, map_function):
        result = Set(self.get_key)
        for element in self:
            new_element = map_function(element)
            result.add(new_element)
        return result
    
    def node_search(self, key):
        node = self.storage_root
        while (node != None):
            node_key = self.get_key(node.data)
            if node_key == key:
                return node
            elif key > node_key:
                node = node.right
            else:
                node = node.left
        return node
    
    def remove(self, key):
        self.remove_node(self.node_search(key))

    def remove_node(self, node_to_remove):
        if node_to_remove != None:
            if node_to_remove.left != None and node_to_remove.right != None:
                successor = node_to_remove.get_successor()
                dataCopy = successor.data
                self.remove_node(successor)
                node_to_remove.data = dataCopy
            elif node_to_remove is self.storage_root:
                if node_to_remove.left != None:
                    self.storage_root = node_to_remove.left
                else:
                    self.storage_root = node_to_remove.right
                if self.storage_root:
                    self.storage_root.parent = None
            elif node_to_remove.left != None:
                node_to_remove.parent.replace_child(node_to_remove, node_to_remove.left)
            else:
                node_to_remove.parent.replace_child(node_to_remove, node_to_remove.right)

    def search(self, key):
        node = self.node_search(key)
        if node != None:
            return node.data
        return None
    
    def union(self, other_set):
        result = Set(self.get_key)
        for element in self:
            result.add(element)
        for element in other_set:
            result.add(element)
        return result