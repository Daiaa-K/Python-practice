class Node:
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev


class DoubleLinkedList:
    #initlazing the list
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None, prev=self.head)
        self.head.next = self.tail
        self.size = 0

    # checking if list is empty
    def is_empty(self):

        return self.size == 0

    # method for printing the list without removing any elements
    def display(self):
        if self.is_empty():
            print("list is empty")
            return
        current = self.head.next
        for i in range(self.size):
            print(current.data, end=" ")
            current = current.next

    # method for removing node from the list
    def remove(self, node: Node):
        nex = node.next
        pre = node.prev
        nex.prev = pre
        pre.next = nex
        self.size -= 1

    # adding a new node in a list
    def add_between(self, data, nex: Node, pre: Node):
        new = Node(data, nex, pre)
        pre.next = new
        nex.prev = new
        self.size += 1

    # adding node at the end of the list
    def add_item_last(self, data):
        if self.is_empty():
            self.add_between(data, self.tail, self.head)
        else:
            self.add_between(data, self.tail, self.tail.prev)

    # adding node at the beginning of the list
    def add_item_first(self, data):
        if self.is_empty():
            self.add_between(data, self.tail, self.head)
        else:
            self.add_between(data, self.head.next, self.head)

    # removing the first element in the lis
    def remove_first(self):
        if self.is_empty():
            print("list is empty")
            return
        current = self.head.next.data
        self.remove(self.head.next)
        return current

    # removing the last element in the list
    def remove_last(self):
        if self.is_empty():
            print("list is empty")
            return
        current = self.tail.prev.data
        self.remove(self.tail.prev)
        return current
