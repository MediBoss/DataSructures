class Node(object):
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

    def __repr__(self):
        return "Node: {}".format(self.data)

class Stack(object):
    def __init__(self, iterable=None):
        if iterable is not None:
            for data in iterable:
                self.push(data)
            return
        self.top = None
        self.counter = 0

    # Retruns an integer that represents the length of the stack
    def size():
        return self.counter

    # Checks if the sack is empty or not
    def isEmpty():
        return self.head == None

    # inserts  a data on top of the stack
    def push(data):
        node = Node(data)
        node.next = self.top
        self.top = node
        self.counter += 1

    # Pops off the node on top of the stack and returns its data
    def pop():
        self.top = self.top.next
        self.counter -= 1
        return top.data

    # Returns the data at the top of the stack
    def peek():
        return self.top.data
