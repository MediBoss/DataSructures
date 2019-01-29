class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

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
        new_node = Node(data)
        # check if the top node is not empty
        if self.top:
            new_node.next = self.top
            self.top = new_node
            self.counter += 1
        # if there is no top, we put the new node at the top
        else:
            self.top = new_node
            self.counter += 1

    # Pops off the node on top of the stack and returns its data
    def pop(self):
        if self.isEmpty() is True:
            return

        else:
            data = self.top.data
            self.size -= 1
            # checks if there's an element after the top node
            if self.top.next:
                self.top = self.top.next
            # if there isn't
            else:
                self.top = None
            return data
            
        return data

    # Returns the data at the top of the stack
    def peak(self):
        if self.isEmpty() is True:
            return None

        return self.top.data
