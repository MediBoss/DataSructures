class Node(object):

    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "Node with data {}".format(self.data)

class Queue(object):

    def __init__(self, iterator=None):
        if iterator is not None:
            for data in iterator:
                self.enqueue(data)

        self.front = None
        self.back = None
