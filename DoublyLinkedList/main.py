from doubly_linked_list import DoublyLinkedList
from doubly_linked_list import Node

def main():
    list = DoublyLinkedList()
        # Testing isEmpty() method
    print(list.isEmpty())
    list.insertHead("medi")
    print(list.isEmpty())



if __name__ == '__main__':
    main()
