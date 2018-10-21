
from doubly_linked_list import DoublyLinkedList
from doubly_linked_list import Node
import unittest

class TestDoublyLinkedList(unittest.TestCase):

    def test_init(self):
        dll = DoublyLinkedList()
        assert dll.head is None
        assert dll.tail is None
        assert dll.counter == 0

    def test_print_list(self):
        list = DoublyLinkedList()
        list.printLinkedList()
        list.insertHead("Medi")
        list.insertHead("Yves")
        list.insertHead("Jonas")
        list.printLinkedList()


    # Testing insterHead and insertTail Methods
    def test_data_insertion(self):
        list = DoublyLinkedList()
        list.insertHead("Medi")
        list.insertHead("Yves")
        list.insertHead("Jonas")
        assert list.isEmpty() is False
        assert list.length() == 3
        assert list.find("Yves") is True
        assert list.find("Marc") is False




if __name__ == '__main__':
        unittest.main()
