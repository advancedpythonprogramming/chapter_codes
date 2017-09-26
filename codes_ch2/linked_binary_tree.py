class Node:

    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent
        self.left_child = None
        self.right_child = None

    def __repr__(self):
        return 'parent: {0}, value: {1}'.format(self.parent, self.value)


class BinaryTree:

    def __init__(self, root_node=None):
        self.root_node = root_node

    def add_node(self, value):
        if self.root_node is None:
            self.root_node = Node(value)
        else:
            temp = self.root_node
            added = False

            while not added:
                if value <= temp.value:
                    if temp.left_child is None:
                        temp.left_child = Node(value, temp.value)
                        added = True

                    else:
                        temp = temp.left_child

                else:
                    if temp.right_child is None:
                        temp.right_child = Node(value, temp.value)
                        added = True

                    else:
                        temp = temp.right_child

    def __repr__(self):
        def traverse_tree(Node, side="root"):
            ret = ''

            if Node is not None:
                ret += '{0} -> {1}\n'.format(Node, side)
                ret += traverse_tree(Node.left_child, 'left')
                ret += traverse_tree(Node.right_child, 'right')

            return ret

        return traverse_tree(self.root_node)


if __name__ == '__main__':
    T = BinaryTree()
    T.add_node(4)
    T.add_node(1)
    T.add_node(5)
    T.add_node(3)
    T.add_node(20)

    print(T)
