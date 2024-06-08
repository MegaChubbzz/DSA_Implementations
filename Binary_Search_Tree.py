'''Implementing a binary search tree'''


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def search(self, desired_key):
        current_node = self.root
        while current_node is not None:
            if current_node.key == desired_key:
                return current_node
            elif desired_key < current_node.key:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return None

    def insert(self, node):
        if self.root is None:
            self.root = node
        else:
            current_node = self.root
            while current_node is not None:
                if node.key < current_node.key:
                    if current_node.left is None:
                        current_node.left = node
                        current_node = None
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = node
                        current_node = None
                    else:
                        current_node = current_node.right

    def remove(self, key):
        parent = None
        current_node = self.root
        while current_node is not None:
            if current_node.key == key:
                if current_node.left is None and current_node.right is None:
                    if parent is None:
                        self.root = None
                    elif parent.left is current_node:
                        parent.left = None
                    else:
                        parent.right = None
                    return
                elif current_node.left is not None and current_node.right is None:
                    if parent is None:
                        self.root = current_node.left
                    elif parent.left is current_node:
                        parent.left = current_node.left
                    else:
                        parent.right = current_node.left
                    return
                else:
                    successor = current_node.right
                    while successor.left is not None:
                        successor = successor.left
                    current_node.key = successor.key
                    parent = current_node
                    current_node = current_node.right
                    key = parent.key
            elif current_node.key < key:
                parent = current_node
                current_node = current_node.right
            else:
                parent = current_node
                current_node = current_node.left
        return
