from doubly_linked_list import DoublyLinkedList
from doubly_linked_list import Node
import unittest

class TestNode(unittest.TestCase):

    def test_init(self):
        data = "ABC" # assuming that data in the list are strings
        node = Node(data)

class TestDoublyLinkedList(unittest.TestCase):

    def test_init(self):
        dll = DoublyLinkedList()
        assert dll.head is None
        assert dll.tail is None
        assert dll.counter == 0

    def test_length(self):
        dll = DoublyLinkedList
        assert dll.length() == 0
        dll.append()



if __name__ == '__main__':
    unittest.main()
