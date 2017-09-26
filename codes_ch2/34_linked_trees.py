# 34_linked_trees.py

class Tree:
    # We create the basic structure of the tree. Children nodes can be keep in
    # a different data structure, such as: a lists or a dictionary. In this
    # example we manage the children nodes in a dictionary.

    def __init__(self, node_id, value=None, parent_id=None):
        self.node_id = node_id
        self.parent_id = parent_id
        self.value = value
        self.children = {}

    def add_node(self, node_id, value=None, parent_id=None):
        # Every time that we add a node, we need to verify the parent of the
        # new node. If it is not the parent, we search recursively through the
        # the tree until we find the right parent node.

        if self.node_id == parent_id:
            # If the node is the parent, we update the dictionary with the
            # children.
            self.children.update({node_id: Tree(node_id, value, parent_id)})
        else:
            # If the node is not the parent we search recursively
            for child in self.children.values():
                child.add_node(node_id, value, parent_id)

    def get_node(self, node_id):
        # We recursively get the node as long as it exists in the tree.
        if self.node_id == node_id:
            return self
        else:
            for child in self.children.values():
                node = child.get_node(node_id)
                if node:
                    # if the node exists in the tree, returns the node
                    return node

    def __repr__(self):
        # We override this method in order to traverse recursively the node in
        # the tree.
        def traverse_tree(root):
            ret = ''
            for child in root.children.values():
                ret += "id-node: {} -> parent_id: {} -> value: {}\n".format(
                    child.node_id, child.parent_id, child.value)
                ret += traverse_tree(child)
            return ret

        ret = 'root:\nroot-id: {} -> value: {}\n\nchildren:\n'.format(
            self.node_id, self.value)
        ret += traverse_tree(self)

        return ret


if __name__ == '__main__':
    T = Tree(0, 10)
    T.add_node(1, 8, 0)
    T.add_node(2, 12, 0)
    T.add_node(3, 4, 1)
    T.add_node(4, 9, 1)
    T.add_node(5, 1, 3)
    T.add_node(6, 18, 2)

    # We show the tree as we define in the __repr__ method.
    print(T)

    print()

    node = T.get_node(6)
    print('The ID of the node is {}'.format(node))

    node = T.get_node(1)
    print('The node has {} children'.format(len(node.children)))
