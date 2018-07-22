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
    def size(self):
        return self.counter

    # Checks if the sack is empty or not
    def isEmpty(self):
        return self.top is None

    # inserts  a data on top of the stack
    def push(self,data):
        new_node = Node(data, self.top)
        self.top = new_node
        self.counter += 1

    # Pops off the node on top of the stack and returns its data
    def pop(self):
        if self.isEmpty() is True:
            return

        old_top = self.top
        self.top = self.top.next
        self.counter -= 1
        return old_top.data

    # Returns the data at the top of the stack
    def peak(self):
        if self.isEmpty() is True:
            return None

        return self.top.data
