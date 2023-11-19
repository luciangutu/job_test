# Linked list implementation in Python


class Node:
    # Creating a node
    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    # Search an element
    def search(self, key):
        current = self.head
        while current is not None:
            if current.item == key:
                return True
            current = current.next
        return False


if __name__ == '__main__':

    linked_list = LinkedList()

    # Assign item values
    linked_list.head = Node(1)
    second = Node(2)
    third = Node(3)
    forth = Node("a")
    fifth = Node(["x", "y", "z"])

    # Connect nodes
    linked_list.head.next = second
    second.next = third
    third.next = forth
    forth.next = fifth

    item_to_find = 3
    if linked_list.search(item_to_find):
        print(str(item_to_find) + " is found")
    else:
        print(str(item_to_find) + " is not found")

    # Print the linked list item
    while linked_list.head is not None:
        print(linked_list.head.item, end=" ")
        linked_list.head = linked_list.head.next

