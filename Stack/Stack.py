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
        
    # Checks if the sack is empty or not
    def isEmpty():
        return self.head == None

    # inserts  a data on top of the stack
    def push(data):
        node = Node(data)
        node.next = self.top
        self.top = node

    # Pops off the node on top of the stack and returns its data
    def pop():
        self.top = self.top.next
        return top.data

    # Returns the data at the top of the stack
    def peek():
        return self.top.data
