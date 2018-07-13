
class Node:

    def __init__(self,data):
        self.data = Data
        self.next = None
        self.prev = None
        
class DoublyLinkedList:

    def __init__(self):
        if isinstance(head, Node) and isinstance(tail, Node):
            self.head = None

    def list_of_items(self):
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

    def isEmpty(self):
        return self.head is None
    
    def append(self, data):


        new_node = Node(data)
        new_node.next = None # since it will be the last node in the list
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next

            current_node.next = new_node
            new_node.prev = current_node
            return

        def prepand(self, data):
            new_node = Node(data)
            new_node.next = self.head
            if isEmpty() is False:
                self.head.prev = new_node
            self.head = new_node
