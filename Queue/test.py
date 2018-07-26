
from LinkedQueue import Node, Queue
import unittest

class Test_Queue(unittest.TestCase):

    def test_init(self):
        queue = Queue()

        assert queue.front is None
        assert queue.rear is None

    def test_general(self):
        queue = Queue()

        assert queue.isEmpty() is True
        assert queue.size() == 0

        queue.enqueue("Medi")
        queue.enqueue("Yves")
        queue.enqueue("Martial")

        assert queue.isEmpty() is False
        assert queue.size() == 3

        queue.dequeue()
        
        assert queue.size() == 2


if __name__ == '__main__':
    unittest.main()
