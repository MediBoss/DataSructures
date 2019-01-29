'''
    A Node-Based implementation of the Queue Data Struture
'''
from LinkedList import LinkedList
class Node(object):

    def __init__(self,data):
        self.data = data
        self.next = None

class Queue(object):

    def __init__(self):

        self.front = None
        self.rear = None
        self.counter = 0

    # Function to return the length of the queue
    def size(self):
        return  self.counter

    def isEmpty(self):
        ''' Check wheater or not the list empty'''

        return (self.front == None and self.rear == None)


    def enqueue(self, data):
        ''' Add an object at the back of the queue'''

        temp = Node(data)
        if self.isEmpty():
            self.front = self.rear = temp
            self.counter += 1
            return

        self.rear.next = temp
        self.rear = temp
        self.counter += 1

    def dequeue(self):
        ''' Function to remove and return the object at the front of the queue '''

        temp = self.front
        if self.isEmpty():
            return
        elif self.front == self.rear:
            self.front = self.rear = None
            self.counter -= 1
            return temp
        else:
            self.front = self.front.next
            self.counter -= 1
            return temp
