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
        self.counter = 0

    # Function to return the length of the queue
    def size(self):
        return self.counter

    # Function to to check wheater or not the list empty
    def isEmpty(self):
        return self.front is None

    # Function to add an object at the back of the queue
    def enqueue(self, data):

    # Function to remove and return the object at the front of the queue
    def dequeue(self):
        if self.isEmpty() is True:
            return None
        else:
            temp = Node(data):
            



    # Function to retrun the object at the front of the queue
    def peak(self):
