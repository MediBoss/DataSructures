
from doubly_linked_list import DoublyLinkedList
from doubly_linked_list import Node
import unittest

class TestDoublyLinkedList(unittest.TestCase):

    def test_init(self):
        dll = DoublyLinkedList()
        assert dll.head is None
        assert dll.tail is None
        assert dll.counter == 0

    def test_general(self):
        list = DoublyLinkedList()
        list.insertHead("Medi")
        list.insertHead("Yves")
        list.insertHead("Jonas")
        assert list.isEmpty() is False
        assert list.length() == 3



if __name__ == '__main__':
        unittest.main()
