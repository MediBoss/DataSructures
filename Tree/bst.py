class Node:
    ''' Implement a Node'''
    def __init__(self, data):
        ''' Initialize a Node with a data, left and right child'''
        self.data = data
        self.left = None
        self.right = None


class BST:
    ''' Implement a Binary Search Tree'''

    def __init__(self):
        self.root = None


    # insert

    # remove

    # traverse

    # minimum
    def min(self):
        ''' Return the node with the minimum value
            Time Complexity : O(h) where h is the height of tree
            Space Complexity : O(1)
        '''
        current = self.root
        while current.left != None:
            current = current.left

        return current

    # maximum
    def max(self):
        pass
