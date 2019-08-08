
class Node(object):

    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "Node with data {}".format(self.data)

class LinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None
        self.counter = 0

    # Getter methods
    def getHead(self):
        return self.head

    def getTails(self):
        return self.tail


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

    # This function replaces a data from the list with a new one
    def replace(self, old_item, new_item):
        if self.isEmpty is True:
            return "The list is Empty"
        else:
            new_node = Node(new_item)
            temp_node = self.head
            if new_node.data == self.head.data:
                self.head.data = new_item
            else:
                temp_node.data == self.tail.data
                self.tail.data  = new_item
            while(temp_node is not None):
                temp_node = temp_node.next
                if temp_node.data == old_item:
                    temp_node.data = new_item
                else:
                    return "Data Not Found"

    # This function returns the size of the list
    def length(self):
        return self.counter

    # This function adds the data given at the end of the list
    def insertTail(self, data):
        temp = Node(data)
        if self.isEmpty() is True:
            self.head = temp
            self.counter += 1

        else:
            self.tail.next = temp
            self.tail = temp
            self.counter += 1


        # This function adds the data given at the beginning of the list
    def insertHead(self, data):
        new_node = Node(data)
        if self.isEmpty() == True:
            self.tail = temp
        else:
            temp.next = self.head
        self.head = temp

    #This function deletes the head Node from the list
    def deleteHead(self):
        temp_node = self.head
        self.head = self.head.next
        self.head.prev = None
        if self.head == None:
            self.tail = None
            print "The List is Empty"
        self.counter -= 1
        return temp_node
