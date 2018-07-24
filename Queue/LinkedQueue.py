from LinkedList import Node
from LinkedList import LinkedList

class Queue(object):

    def __init__(self, iterator=None):

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
        pass

    # Function to remove and return the object at the front of the queue
    def dequeue(self):
        pass

    # Function to retrun the object at the front of the queue
    def front(self):
        pass

    # Function to return the object at the tail of the queue
    def rear(self):
        pass
