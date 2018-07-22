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

    def isEmpty():
        return self.head == None

    def push(data):
        node = Node(data)
        node.next = self.top
        self.top = node

    def pop():
        
