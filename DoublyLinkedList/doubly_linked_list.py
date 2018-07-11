
    # The node class
class Node:

    def __init__(self,data):
        self.data = Data
        self.next = None
        self.prev = None

        # The doubly linked list class
class DoublyLinkedList:

    def __init__(self):
        """Initialize this doubly linked list ."""
        if isinstance(head, Node) and isinstance(tail, Node):
            self.head = None

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
        return self.head is None

    # This function adds teh data given at the end of the list
    def append(self, data):
        """Insert the given item at the tail of this linked list."""

        new_node = Node(data)
        new_node.next = None # since it will be the last node in the list

        #If the list is empty...
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return
        # if the list is not empty
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next

            current_node.next = new_node
            new_node.prev = current_node
            return

        # This function adds teh data given at the beginning of the list
        def prepand(self, data):
            new_node = Node(data)
            new_node.next = self.head
            if !isEmpty():
                self.head.prev = new_node
            self.head = new_node
