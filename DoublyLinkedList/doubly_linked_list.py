
    # The node class
class Node(object):

    next = None
    previous = None

    def __init__(self,data):
        self.data = data

    def representation(self):
        return "Node with data of {} ".fomat(self.data)

        # The doubly linked list class
class DoublyLinkedList(object):

    length = 0 # class attribute

    def __init__(self, items = None):
        """Initialize this doubly linked list ."""
        self.head = None
        self.tail = None

    def string_representation(self):
        """Return a formatted string representation of this linked list."""
        return "Doubly linked list with {} elemnets".fromat(DoublyLinkedList.length)

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

    def append(self,item):
        """Insert the given item at the tail of this linked list."""
        temporary_node = Node(item) # creates a new node with the data passed O(1)
        temporary_node.next = None # Sets its pointer to a value of nothing
        self.tail.next = temporary_node # next pointer of tail links to the temp.node
        temporary_node.previous = self.tail # the previous node of temp.node now links to former tail
        self.tail = temporary_node # now temp node is the tail

    def prepend(self,item):
        """Insert the given item at the head of this linked list.
        Best and worst case running time: ??? under what conditions? [TODO]"""

    def find(self,item):
        """Return an item from this linked list satisfying the given quality"""


    def replace(self, old_item, new_item):
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
