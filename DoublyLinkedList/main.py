from doubly_linked_list import DoublyLinkedList
from doubly_linked_list import Node

def main():
    test()

def test():
    list = DoublyLinkedList()
    print(list.isEmpty()) # prints True
    list.insertHead("hello") # inseart new data
    print(list.isEmpty()) # prints false
    list.delete("holla")
    #list.insertHead("hi")
    #List.insertHead("bonjour")


if __name__ == '__main__':
    main()
