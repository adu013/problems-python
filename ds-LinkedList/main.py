# LinkedList/main.py
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.root = None

    def length(self):
        if self.root == None:
            return 0
        else:
            current_node = self.root
            node_nos = 1
            while True:
                if current_node.next is None:
                    break
                current_node = current_node.next
                node_nos += 1
            return node_nos


    def insert(self, newNode):
        if self.root == None:
            self.root = newNode
        else:
            lastnode = self.root
            while True:
                if lastnode.next is None:
                    break
                lastnode = lastnode.next
            lastnode.next = newNode

    def insert_head(self, newNode):
        tempnode = Node()
        tempnode = self.root
        self.root = newNode
        self.root.next = tempnode

    def insert_at(self, new_node, position):
        if position < 0 or position > self.length():
            print("Invalid position")
            return
        if position == 0:
            self.insert_head(new_node)
            return
        current_node = self.root
        current_pos = 0
        while True:
            if current_pos == position:
                previous_node.next = new_node
                new_node.next = current_node
                break
            previous_node = current_node
            current_node = current_node.next
            current_pos += 1

    def delete_end(self):
        current_node = self.root
        if current_node is None:
            print("List is already empty")
            return
        while True:
            if current_node.next is None:
                previous_node.next = None
                break
            previous_node = current_node
            current_node = current_node.next

    def delete_at(self, pos):
        current_node = self.root
        current_pos = 1
        if current_node is None:
            print("List is already empty")
            return
        if pos <= 0 or pos > self.length():
            print("Invalid position")
            return
        if pos == 1:
            self.root = current_node.next
            return
        while True:
            if current_pos == pos:
                previous_node.next = current_node.next
                break
            previous_node = current_node
            current_node = current_node.next
            current_pos += 1

    def print(self):
        currentnode = self.root
        if currentnode is None:
            print("List is empty")
        while True:
            if currentnode is None:
                break
            print(currentnode.value)
            currentnode = currentnode.next


# Building a linked list
firstnode = Node("Tom")
linkedlist = LinkedList()
linkedlist.insert(firstnode)
secondnode = Node("Bill")
linkedlist.insert(secondnode)
thirdnode = Node("Ben")
linkedlist.insert(thirdnode)
headnode = Node("Jim")
linkedlist.insert_head(headnode)
middlenode = Node("Mary")
linkedlist.insert_at(middlenode, 2)


# printing the linked list
linkedlist.print()
print("Length: " + str(linkedlist.length()))
print("**********************************")

# delete node
linkedlist.delete_end()
linkedlist.print()
print("**********************************")

# delete node at position
linkedlist.delete_at(1)
linkedlist.print()
