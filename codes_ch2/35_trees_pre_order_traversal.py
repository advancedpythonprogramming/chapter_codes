from linked_tree import Tree
# 35_trees_pre_order_traversal.py

class TreePreOrder(Tree):
    # We inherited the original class of our linked tree, and override the
    # __repr__ method to traverse the tree using pre-order traversal.

    def __repr__(self):
        def traverse_tree(root):
            ret = ''
            # We first visit the root note
            ret += "node_id: {}, parent_id: {} -> value: {}\n".format(
                root.node_id, root.parent_id, root.value)
            
            # And finally, we traverse the children recursively
            for child in root.children.values():
                ret += traverse_tree(child)

            return ret

        return traverse_tree(self)


if __name__ == '__main__':
    # We add some nodes to the tree
    T = TreePreOrder(0, 10)
    T.add_node(1, 8, 0)
    T.add_node(2, 12, 0)
    T.add_node(3, 4, 1)
    T.add_node(4, 4, 1)
    T.add_node(5, 1, 3)
    T.add_node(6, 18, 2)

    print(T)
