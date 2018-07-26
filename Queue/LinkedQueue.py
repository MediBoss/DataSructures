'''
    A LinkedList-style implementation of the Queue Data Struture
'''
class Node(object):

    def __init__(self,data):
        self.data = data
        self.next = None

class Queue(object):

    def __init__(self, iterator=None):

        self.front = None
        self.rear = None
        self.counter = 0

    # Function to return the length of the queue
    def size(self):
        return  self.counter

    # Function to to check wheater or not the list empty
    def isEmpty(self):
        return (self.front == NULL and self.rear == NULL)

    # Function to add an object at the back of the queue
    def enqueue(self, data):

        temp = Node(data)
        if self.isEmpty():
            self.front = self.rear = temp
            return

        self.rear.next = temp
        self.rear = temp

    # Function to remove and return the object at the front of the queue
    def dequeue(self):
        pass

    # Function to retrun the object at the front of the queue
    def front(self):
        pass

    # Function to return the object at the tail of the queue
    def rear(self):
        pass
