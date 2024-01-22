from linked_list import DoubleLinkedList as ls
from stack import Stack

if __name__ == '__main__':
    # -- The linked List --
    l = ls()
    # adding numbers to the list
    for i in range(5):
        l.add_item_first(i)
    l.display()
    print()
    # removing elements from the list
    for i in range(l.size):
        print(l.remove_last(), end=" ")
    print()
    l.display()
    print("------------------------------------")
    # -- The stack --
    s = Stack()
    # adding numbers to the stack
    for i in range(5):
        s.push(i)
    # popping elements from the stack
    for i in range(s.len()):
        print(s.pop(), end=" ")
