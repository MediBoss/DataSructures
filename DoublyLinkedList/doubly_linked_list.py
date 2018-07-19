
    # The node class
class Node(object):

    def __init__(self,data):
        self.data = Data
        self.next = None
        self.prev = None

        # The doubly linked list class
class DoublyLinkedList(object):

    counter  = 0
    def __init__(self):
        self.head = None
        self.tail = None

    # function that retruns a boolean value if the list is empty or not
    def isEmpty(self):
        return self.head == None

    def printLinkedList(self):
        if self.isEmpty() == True:
            print "The list is Empty"
            return
        else:
            temp_node = self.head
            while(temp_node.next != None):
                print(temp_node.data)

    # This functions retruns a boolean on wheter or not the data is found in the list
    def find(self, data):
        if self.isEmpty() == True:
            print "The List is empty"
        else:
            temp_node = self.head # start from the head node
            while temp_node is not None:
                if temp_node.data == data:
                    return True
                temp_node = temp_node.next
            return False


    def replace(self, old_item, new_item):

    def length(self):


    # This function adds the data given at the end of the list
    def insertTail(self, data):
        new_node = Node(data)
        new_node.next = None
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.counter += 1

    def deleteTail(self):
        if self.isEmpty() == True:
            print "The List is Empty"
        else:
            temp_node = self.head
            self.tail = self.tail.prev
            self.tail.next = None
            self.counter -= 1
            return temp

        # This function adds the data given at the beginning of the list
    def insertHead(self, data):
        new_node = Node(data)
        if self.isEmpty() == True:
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.counter += 1

    #This function deletes the head Node from the list
    def deleteHead(self):
        temp_node = self.head
        self.head = self.head.next
        self.head.prev = None
        if self.isEmpty() == True:
            self.tail = None
            print "The List is Empty"
        self.counter -= 1
        return temp

    #This function deletes a Node from the list given a data
    def delete(self, data):
        if self.isEmpty() == True:
            print "The List is Empty"
            return
        else:
            temp_node = self.head
            while(temp_node.data != data):
                # looking for the node that has the data to be deleted
                temp_node = temp_node.next
            if temp_node == self.head:
                self.deleteHead()
            elif temp_node == self.tail:
                self.deleteTail()
            else:
                temp_node.prev.next = temp_node.next
                temp_node.next.prev = temp_node.prev
