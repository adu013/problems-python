# BinarySearchTree/main.py
class Node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, current_node):
        if value < current_node.value:
            if current_node.left_child == None:
                current_node.left_child = Node(value)
                current_node.left_child.parent = current_node
            else:
                self._insert(value, current_node.left_child)
        elif value > current_node.value:
            if current_node.right_child == None:
                current_node.right_child = Node(value)
                current_node.right_child.parent = current_node
            else:
                self._insert(value, current_node.right_child)
        else:
            print("Duplicate value")

    def print(self):
        if self.root != None:
            self._print(self.root)

    def _print(self, current_node):
        if current_node != None:
            self._print(current_node.left_child)
            print(str(current_node.value))
            self._print(current_node.right_child)

    def height(self):
        if self.root != None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, current_node, current_height):
        if current_node == None:
            return current_height
        left_height = self._height(current_node.left_child, current_height+1)
        right_height = self._height(current_node.right_child, current_height+1)
        return max(left_height, right_height)

    def search(self, value):
        if self.root != None:
            return self._search(value, self.root)
        else:
            return False

    def _search(self, value, current_node):
        if value == current_node.value:
            return True
        elif value < current_node.value and current_node.left_child != None:
            return self._search(value, current_node.left_child)
        elif value > current_node.value and current_node.right_child != None:
            return self._search(value, current_node.right_child)
        return False

    def find(self, value):
        if self.root != None:
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value, current_node):
        if value == current_node.value:
            return current_node
        elif value < current_node.value and current_node.left_child != None:
            return self._find(value, current_node.left_child)
        elif value > current_node.value and current_node.right_child != None:
            return self._find(value, current_node.right_child)

    def delete(self, value):
        return self._delete_node(self.find(value))

    def _delete_node(self, node):

        # returns the node with min value in tree rooted at input node
        def min_value_node(n):
            current = n
            while current.left_child != None:
                current =  current.left_child
            return current

        def num_children(current_node):
            """
            returns the number of children for specific node
            :param n node
            """
            num_children = 0
            if current_node.left_child != None:
                num_children += 1
            if current_node.right_child != None:
                num_children += 1
            return num_children

        # get the parent of the node to be deleted
        node_parent = node.parent

        # get the number of children of the node to be deleted
        node_children = num_children(node)

        # Deleting node according to cases
        # Case 1: node has no children
        if node_children == 0:
            if node_parent.left_child == node:
                node_parent.left_child = None
            else:
                node_parent.right_child = None

        # Case 2: (node has 1 child)
        if node_children == 1:
            # get the child node
            if node.left_child != None:
                child = node.left_child
            else:
                child = node.right_child

            # replace the node
            if node_parent.left_child == node:
                node_parent.left_child = child
            else:
                node_parent.right_child = child

            # correct the parent pointer in node
            child.parent = node_parent

        # Case 3: (node has 2  children)
        if node_children == 2:

            # get the inorder successor of the deleted node
            successor = min_value_node(node.right_child)

            node.value = successor.value

            self._delete_node(successor)

'''
def fill_tree(tree, num_elements=100, max_int=1000):
    from random import randint
    for _ in range(num_elements):
        curr_elem = randint(0, max_int)
        tree.insert(curr_elem)
    return tree

tree = BinarySearchTree()
tree = fill_tree(tree)

tree.print()
print("Tree height: " + str(tree.height()))
print(tree.search(559))
'''
