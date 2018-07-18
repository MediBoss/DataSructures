
    # The node class
class Node:

    def __init__(self,data):
        self.data = Data
        self.next = None
        self.prev = None

        # The doubly linked list class
class DoublyLinkedList:

    def __init__(self):
            self.head = None
            self.tail = None

    def list_of_items(self):
         """Return a list of all items in this linked list"""
         assert(is_empty() == True), "The list is empty"
         try:
             list_to_be_returned = []
             temporary_node = self.head # starting with the head node
             while temporary_node is not None:
                 list_to_be_returned.append(temporary_node.data)
                 temporary_node = temp_node.next

         except TypeError,IndexError:
             print "Error Occured : Either Null value found or index out of bound"

         return list_to_be_returned

    # function that retruns a boolean value if the list is empty or not
    def isEmpty(self):
        return self.head == None

    # This function adds teh data given at the end of the list
    def append(self, data):
        new_node = Node(data)
        new_node.next = None
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

        # This function adds the data given at the beginning of the list
    def prepand(self, data):
        new_node = Node(data)
        if isEmpty() == True:
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    #This function deletes the head Node from the list
    def deleteHead(self):
        if isEmpty() == True:
            return "List is Empty"
        else:
            temp_node = self.head
            temp_node.prev = None
            self.head  = temp_node
