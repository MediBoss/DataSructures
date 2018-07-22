import unittest
from Stack import Stack, Node

class TestStack(unittest.TestCase):
    def test_init(self):
        stack = Stack()
        assert stack.top is None

    def test_general(self):
        stack = Stack()
            #Testing size ()and isEmpty()
        assert stack.size() == 0
        assert stack.isEmpty() == True

        #Testing push(), peak(), and pop()
        stack.push('M')
        stack.push('E')
        stack.push('D')
        stack.push('I')
        assert stack.peak() == 'I'
        assert stack.size() == 4
        stack.pop()
        assert stack.size() == 3
        stack.pop()
        assert stack.size() == 2
        assert stack.isEmpty() is False
        assert stack.peak() == 'E'
        assert stack.size() == 2





if __name__ == '__main__':
    unittest.main()
