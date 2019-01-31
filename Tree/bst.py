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
    def insert(self, target_data):

        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        current = self.node
        parent = None
        while True:
            parent = current
            if node.data < current.data:
                current = current.left
                if current is None:
                    parent.left = new_node
                    return
            else:
                current = current.right
                if current is None:
                    parent.right = new_node
                    return


    def recursive_insert(self, root, data):
        ''' Insert a node in the Binary Search Tree recursively
            Time Complexity : O(h) where h is the height of tree
            Space Complexity : O(1)
        '''
        if root is None:
            new_node = Node(data)
            root = new_node
            return
        else:
            new = node = Node(data)
            if data <= root.left:
                if root.left:
                    self.recursive_insert(root.left, data)
                else:
                    root.left = new_node
            else:
                if root.right:
                    self.recursive_insert(root.right, data)
                else:
                    root.right = new_node


    # remove
    def remove(self, node):
        pass

    # DEPTH FIRST SEARCH
    def inoder(self, root_node, data):
        ''' Traverse the Tree from left child to root finishing with right child'''

        current = root_node
        if current is None:
            return
        self.inoder(root_node.left, data)
        print(current.data)
        self.inoder(root_node.right, data)

    def preorder(self, root_node, data):
        ''' Traverse the Tree from root to left child finishing with right child'''

        current = root_node
        if current:
            print(current.data)
            self.preorder(current.left, data)
            self.preorder(current.right, data)

def postorder(self, root_node, data):
    ''' Traverse the Tree from right child to left child finishing with root'''

    current = root_node
    if current:
        self.postorder(current.left)
        self.postorder(current.right)
        print(current.data)

    # height

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
