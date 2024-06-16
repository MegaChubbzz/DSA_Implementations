class Node234:
    def __init__(self, key_A, left_child=None, middle1_child=None):
        self.A = key_A
        self.B = None
        self.C = None
        self.left = left_child
        self.middle1 = middle1_child
        self.middle2 = None
        self.right = None

    def get_child(self, child_index):
        if child_index == 0:
            return self.left
        elif child_index == 1:
            return self.middle1
        elif child_index == 2:
            return self.middle2
        elif child_index == 3:
            return self.right
        return None
    
    def get_child_index(self, child):
        if child is self.left:
            return 0
        elif child is self.middle1:
            return 1
        elif child is self.middle2:
            return 2
        elif child is self.right:
            return 3
        return -1
    
    def get_key(self, key_index):
        if key_index == 0:
            return self.A
        elif key_index == 1:
            return self.B
        elif key_index == 2:
            return self.C
        return None
    
    def get_key_index(self, key):
        if key == self.A:
            return 0
        elif key == self.B:
            return 1
        elif key == self.C:
            return 2
        return -1
    
    def append_key_and_child(self, key, child):
        if self.B == None:
            self.B = key
            self.middle2 = child
        else:
            self.C = key
            self.right = child

    def count_keys(self):
        if self.C != None:
            return 3
        elif self.B != None:
            return 2
        return 1
    
    def has_key(self, key):
        return self.A == key or self.B == key or self.C == key
    
    def insert_key(self, key):
        if key < self.A:
            self.C = self.B
            self.B = self.A
            self.A = key
        elif self.B == None or key < self.B:
            self.C = self.B
            self.B = key
        else:
            self.C = key

    def insert_key_with_children(self, key, leftChild, rightChild):
        if key < self.A:
            self.C = self.B
            self.B = self.A
            self.A = key
            self.right = self.middle2
            self.middle2 = self.middle1
            self.middle1 = rightChild
            self.left = leftChild
        elif self.B == None or key < self.B:
            self.C = self.B
            self.B = key
            self.right = self.middle2
            self.middle2 = rightChild
            self.middle1 = leftChild

    def next_node(self, key):
        if key < self.A:
            return self.left
        elif self.B == None or key < self.B:
            return self.middle1
        elif self.C == None or key < self.C:
            return self.middle2
        return self.right
    
    def remove_key(self, key_index):
        if key_index == 0:
            self.A = self.B
            self.B = self.C
            self.C = None
            self.left = self.middle1
            self.middle1 = self.middle2
            self.middle2 = self. right
            self.right = None
        elif key_index == 1:
            self.B = self.C
            self.C = None
            self.middle2 = self.right
            self.right = None
        elif key_index == 2:
            self.C = None
            self.right = None

    def remove_rightmost_child(self):
        removed = None
        if self.right != None:
            removed = self.right
            self.right = None
        elif self.middle2 != None:
            removed = self.middle2
            self.middle2 = None
        return removed
    
    def remove_rightmost_key(self):
        removed = None
        if self.C != None:
            removed = self.C
            self.C = None
        elif self.B != None:
            removed = self.B
            self.B = None
        return removed
    
    def set_child(self, child, child_index):
        if child_index == 0:
            self.left = child
        elif child_index == 1:
            self.middle1 = child
        elif child_index == 2:
            self.middle2 = child
        elif child_index == 3:
            self.right = child

    def set_key(self, key, key_index):
        if key_index == 0:
            self.A = key
        elif key_index == 1:
            self.B = key
        elif key_index == 2:
            self.C = key


class Tree234:
    def __init__(self):
        self.root = None

    def insert(self, key, node=None, node_parent=None):
        if self.root == None:
            self.root = Node234(key)
            return self.root
        if node == None:
            return self.insert(key, self.root, None)
        if node.has_key(key):
            return None
        if node.C != None:
            node = self.split(node, node_parent)
        if not node.is_leaf():
            if key < node.A:
                return self.insert(key, node.left, node)
            elif node.B == None or key < node.B:
                return self.insert(key, node.middle1, node)
            elif node.C == None or key < node.C:
                return self.insert(key, node.middle2, node)
            else:
                return self.insert(key, node.right, node)
        node.insert_key(key)
        return node
    
    def search(self, key):
        return self.search_recursive(key, self.root)
    
    def search_recursive(self, key, node):
        if node == None:
            return None
        if node.has_key(key):
            return node
        if key < node.A:
            return self.search_recursive(key, node.left)
        elif node.B == None or key < node.B:
            return self.search_recursive(key, node.middle1)
        elif node.C == None or key < node.C:
            return self.search_recursive(key, node.middle2)
        return self.search_recursive(key, node.right)
    
    def split(self, node, node_parent):
        split_left = Node234(node.A, node.left, node.middle1)
        split_right = Node234(node.C, node.middle2, node.right)
        if node_parent is not None:
            node_parent.insert_key_with_children(node.B, split_left, split_right)
        else:
            node_parent = Node234(node.B, split_left, split_right)
            self.root = node_parent
        return node_parent
    
    def fuse(self, parent, left_node, right_node):
        if parent is self.root and parent.count_keys() == 1:
            return self.fuse_root()
        left_node_index = parent.get_child_index(left_node)
        middle_key = parent.get_key(left_node_index)
        fused_node = Node234(left_node.A)
        fused_node.B = middle_key
        fused_node.C = right_node.A
        fused_node.left = left_node.left
        fused_node.middle1 = left_node.middle1
        fused_node.middle2 = right_node.left
        fused_node.right = right_node.middle1
        key_index = parent.get_key_index(middle_key)
        parent.remove_key(key_index)
        parent.set_child(fused_node, key_index)
        return fused_node
    
    def fuse_root(self):
        old_left = self.root.left
        old_middle1 = self.root.middle1
        self.root.B = self.root.A
        self.root.A = old_left.A
        self.root.C = old_middle1
        self.root.left = old_left.left
        self.root.middle1 = old_left.middle1
        self.root.middle2 = old_middle1.left
        self.root.right = old_middle1.middle1
        return self.root
    
    def get_min_key(self, node):
        current = node
        while current.left != None:
            current = current.left
        return current.A
        
    def key_swap(self, node, existing, replacement):
        if node == None:
            return False
        key_index = node.get_key_index(existing)
        if key_index == -1:
            next = node.next_node(existing)
            return self.key_swap(next, existing, replacement)
        if key_index == 0:
            node.A = replacement
        elif key_index == 1:
            node.B = replacement
        else:
            node.C = replacement
        return True
    
    def merge(self, node, node_parent):
        node_index = node_parent.get_child_index(node)
        left_sibling = node_parent.get_child(node_index - 1)
        right_sibling = node_parent.get_child(node_index + 1)
        if left_sibling != None and left_sibling.count_keys() >= 2:
            self. rotate_right(left_sibling, node_parent)
        elif right_sibling != None and right_sibling.count_keys() >= 2:
            self.rotate_left(right_sibling, node_parent)
        else:
            if left_sibling == None:
                node = self.fuse(node_parent, node, right_sibling)
            else:
                node = self.fuse(node_parent, left_sibling, node)
        return node
    
    def remove(self, key):
        if self.root.is_leaf() and self.root.count_keys() == 1:
            if self.root.A == key:
                 self.root = None
                 return True
            return False
        current_parent = None
        current = self.root
        while current != None:
            if current.count_keys() == 1 and current is not self.root:
                current = self.merge(current, current_parent)
            key_index = current.get_key_index(key)
            if key_index != -1:
                if current.is_leaf():
                    current.remove_key(key_index)
                    return True
                tmp_child = current.get_child(key_index + 1)
                tmp_key = self.get_min_key(tmp_child)
                self.remove(tmp_key)
                self.key_swap(self.root, key, tmp_key)
                return True
            current_parent = current
            current = current.next_node(key)
        return False
    
    def rotate_left(self, node, node_parent):
        node_index = node_parent.get_child_index(node)
        left_sibling = node_parent.get_child(node_index - 1)
        key_for_left_sibling = node_parent.get_key(node_index - 1)
        left_sibling.append_key_and_child(key_for_left_sibling, node.left)
        node_parent.set_key(node.A, node_index - 1)
        node.remove_key(0)
    
    def rotate_right(self, node, node_parent):
        node_index = node_parent.get_child_index(node)
        right_sibling = node_parent.get_child(node_index + 1)
        key_for_right_sibling = node_parent.get_key(node_index)
        right_sibling.C = right_sibling.B
        right_sibling.B = right_sibling.A
        right_sibling.right = right_sibling.middle2
        right_sibling.middle2 = right_sibling.middle1
        right_sibling.middle1 = right_sibling.left
        right_sibling.A = key_for_right_sibling
        right_sibling.left = node.remove_rightmost_child()
        node_parent.set_key(node.remove_rightmost_key(), node_index)