
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
        self.head = None
        self.tail = None
        self.size = 0


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

    def is_empty(self):
        """Return True if this linked list is empty, or False."""
        return self.head is None

    def length(self):
         """Return the length of this linked list by traversing its nodes."""
         return DoublyLinkedList.length

    def get_at_index(self,index):

        """Return the item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size.
        Best case running time: ??? under what conditions? [TODO]
        Worst case running time: ??? under what conditions? [TODO]"""

    def insert_at_index(self,item):
        """Insert the given item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size.
        Best case running time: ??? under what conditions? [TODO]
        Worst case running time: ??? under what conditions? [TODO]"""

    def append(self, data):
        """Insert the given item at the tail of this linked list."""
            pass

    def prepend(self, data):
        """Insert the given item at the head of this linked list.
        Best and worst case running time: ??? under what conditions? [TODO]"""

            pass

    def find(self, data):
        """Return an item from this linked list satisfying the given quality"""


    def replace(self, old_data, new_data):
        """Replace the given old_item in this linked list with given new_item
        using the same node, or raise ValueError if old_item is not found.
        Best case running time: ??? under what conditions? [TODO]
        Worst case running time: ??? under what conditions? [TODO]"""

    def delete(self,item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case running time: ??? under what conditions? [TODO]
        Worst case running time: ??? under what conditions? [TODO]"""

    def sort_list(self):
        """ Using Quick Sort to sort the list"""
