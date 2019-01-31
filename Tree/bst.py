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

    def min(self):
        ''' Return the node with the minimum value in the Binary Search Tree
            Time Complexity : O(h) where h is the height of tree
            Space Complexity : O(1)
        '''
        current = self.root
        while current.left:
            current = current.left

        return current

    def max(self):
        ''' Return the node with the maximum value in the Binary Search Tree
            Time Complexity : O(h) where h is the height of tree
            Space Complexity : O(1)
        '''
        current = self.root
        while current.right:
            current = current.right

        return current
