from linked_tree import Tree

# 38_trees_depth_first_search.py

class TreeDFS(Tree):
    # We inherited the original class Tree from the previous example and
    # override the __repr__ method to apply the BFS algorithm.

    def __repr__(self):
        def traverse_tree(root):
            ret = ''
            Q = []
            Q.append(root)

            # We use a list to keep the visited nodes
            visited = []

            while len(Q) > 0:
                p = Q.pop()

                if p.node_id not in visited:
                    # We check if the node is in the visited nodes list. If is 
                    # not in the list, we add it
                    visited.append(p.node_id)

                    ret += "node_id: {}, parent_id: {} -> value: {}\n".format(
                        p.node_id, p.parent_id, p.value)
                    for child in p.children.values():
                        Q.append(child)

            return ret
        return traverse_tree(self)


if __name__ == '__main__':
    # We add items to the tree
    T = TreeDFS(0, 10)
    T.add_node(1, 8, 0)
    T.add_node(2, 12, 0)
    T.add_node(3, 4, 1)
    T.add_node(4, 4, 1)
    T.add_node(5, 1, 3)
    T.add_node(6, 18, 2)

    print(T)
