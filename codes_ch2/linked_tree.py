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
        # the tree until we the right parent node.

        if self.node_id == parent_id:
            # If the node is the parent, we update the dictionary with the
            # children.
            self.children.update({node_id: Tree(node_id, value, parent_id)})
        else:
            # If the node is not the parent we search recursively
            for child in self.children.values():
                child.add_node(node_id, value, parent_id)

    def get_node(self, node_id):
        # We recursively get the node as long as it exist in the tree
        # recursivamente obtenemos el node siempre y cuando exista
        # la posicion.

        if self.node_id == node_id:
            return self
        else:
            for child in self.children.values():
                node = child.get_node(node_id)
                if node:
                    # if exist the node in the tree, returns the node
                    return node

    def __repr__(self):
        # We override this method in order to traverse recursively the node in
        # the tree.
        def traverse_tree(root):
            for child in root.children.values():
                self.ret += "id-node: {} -> parent_id: {} -> value: {}\n".format(
                    child.node_id, child.parent_id, child.value)
                traverse_tree(child)
            return self

        self.ret = 'root:\nroot-id: {} -> value: {}\n\nchildren:\n'.format(
            self.node_id, self.value)
        traverse_tree(self)

        return self.ret
