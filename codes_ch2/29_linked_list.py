__author__ = 'cppie_000'
__date__ = '2015.12.17'


class Node:
    # This class models the basic structure, the node.
    def __init__(self, value=None):
        self.next = None
        self.value = value

class LinkedList:
    # This class implement a singly linked list
    def __init__(self):
        self.tail = None
        self.head = None

    def add_node(self, value):
        if not self.head:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

    def __repr__(self):
        rep = ''
        current_node = self.head

        while current_node:
            rep += '{0}'.format(current_node.value)
            current_node = current_node.next
            if current_node:
                rep += ' -> '

        return rep

if __name__ == '__main__':
    l = LinkedList()
    l.add_node(2)
    l.add_node(4)
    l.add_node(7)

    print(l)
