from doubly_linked_list import DoublyLinkedList
from doubly_linked_list import Node

def main():
    test()

def test():
    # Thanks to Make School Unit test's notes on Linked List
    from doubly_linked_list import DoublyLinkedList
    from doubly_linked_list import Node
    import unittest

    class TestNode(unittest.TestCase):

        def test_init(self):
            data = "ABC" # assuming that data in the list are strings
            node = Node(data)
            assert node.data is data
            assert node.next is None

    class TestDoublyLinkedList(unittest.TestCase):

        def test_init(self):
            dll = DoublyLinkedList()
            assert dll.head is None
            assert dll.tail is None
            assert dll.counter == 0

        def test_length(self):
            dll = DoublyLinkedList()
            # Appending and prepnading to increase size
            assert dll.length() == 0
            dll.insertHead("hello")
            assert dll.length() == 1
            dll.insertHead("hi")
            assert dll.length() == 2
            dll.insertTail("howdy")
            assert dll.length() == 3
            dll.insertTail("holla")
            assert dll.length() == 4
            # Deleting to decrease length

            dll.delete("hello")
            #assert dll.length() == 3
            #dll.delete("hi")
            #assert dll.length() == 2
            #dll.delete("howdy")
            #assert dll.length() == 1
            #dll.delete("holla")
            #assert dll.length() == 0

    if __name__ == '__main__':
        unittest.main()


if __name__ == '__main__':
    main()
