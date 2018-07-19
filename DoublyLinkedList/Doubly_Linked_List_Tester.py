from doubly_linked_list import DoublyLinkedList
from doubly_linked_list import Node
import unittest

class TestNode(unittest.TestCase):

    def test_init(self):
        data =
        node = Node(data)

class TestDoublyLinkedList(unittest.TestCase):

    def test_init(self):
        dll = DoublyLinkedList()
        assert dll.head is None
        assert dll.tail is None
        assert dll.size





if __name__ == '__main__':
    unittest.main()
