

    # The node class
class Node(object):

    next_pointer = None # This points to the next node
    prev_pointer = None # This points to the previous node

    def __init__(self,data):
        self.data = data
