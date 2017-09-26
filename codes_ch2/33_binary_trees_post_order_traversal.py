from linked_binary_tree import BinaryTree
# 33_binary_trees_post_order_traversal.py

class BinaryTreePostOrder(BinaryTree):
    # We inherited the original class of our binary tree, and override the
    # __repr__ method to traverse the tree using pre-order traversal.

    def __repr__(self):
        def traverse_tree(node, side="root"):
            ret = ''

            if node is not None:
                ret += traverse_tree(node.left_child, 'left')
                ret += traverse_tree(node.right_child, 'right')                
                ret += '{0} -> {1}\n'.format(node, side)

            return ret
        
        return traverse_tree(self.root_node)


if __name__ == '__main__':
    # We add some nodes to the tree
    T = BinaryTreePostOrder()
    T.add_node(4)
    T.add_node(1)
    T.add_node(5)
    T.add_node(3)
    T.add_node(20)

    print(T)
