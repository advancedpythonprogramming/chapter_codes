from linked_tree import Tree
# 36_trees_post_order_traversal.py

class TreePostOrder(Tree):
    # We inherited the class Tree from te previous example and we override the
    # __repr__ method using the post-order traversal.

    def __repr__(self):
        def traverse_tree(root):
            ret = ''

            # we first recursively traverse the children
            for child in root.children.values():
                ret += traverse_tree(child)

            # Finally, we visit the root note
            string = "node_id: {}, parent_id: {} -> value: {}\n"
            ret += string.format(root.node_id, root.parent_id, root.value)

            return ret

        return traverse_tree(self)


if __name__ == '__main__':
    # We add instances to the tree
    T = TreePostOrder(0, 10)
    T.add_node(1, 8, 0)
    T.add_node(2, 12, 0)
    T.add_node(3, 4, 1)
    T.add_node(4, 4, 1)
    T.add_node(5, 1, 3)
    T.add_node(6, 18, 2)

    print(T)
