class Stack:
    def __init__(self):
        self.data = []

    # adding elements on top of the list
    def push(self, item):
        try:
            self.data.append(item)
        except:
            print(f"failed at adding {item}")
        else:
            print(f"added {item} successfuly")

    # removing elements from top of the list
    def pop(self):
        if self.is_empty():
            print("cant pop from empty stack")
            return
        return self.data.pop()

    # getting the element on top without removing it

    def peek(self):
        if self.is_empty():
            print("stack is empty")
            return
        return self.data[-1]

    # getting size of the list
    def len(self):
        return len(self.data)

    # checking if the list is empty
    def is_empty(self):
        return self.len() == 0
