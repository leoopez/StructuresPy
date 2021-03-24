class TreeNode:
    def __init__(self, data=None, parent=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        return str(self.data)


class BinaryTree:
    def __init__(self, values=None):
        self.root = None
        for v in values:
            self.insert(TreeNode(v))

    def search(self, key) -> object:
        node = self.root
        while node is not None and node.data != key:
            if node.data > key:
                node = node.left
            else:
                node = node.right
        return node

    def insert(self, node) -> None:
        if self.root is None:
            self.root = node
            return
        pos = self.root
        par = pos
        while pos is not None:
            par = pos
            if pos.data < node.data:
                pos = pos.right
            else:
                pos = pos.left

        if par.data < node.data:
            par.right = node
        else:
            par.left = node
        node.parent = par

    def remove(self, node) -> None:
        if node.left is None:
            self.__swap(node, node.right)
        elif node.right is None:
            self.__swap(node, node.left)
        else:
            y = successor(node)
            if y.parent is not node:
                self.__swap(y, y.right)
                y.right = node.right
                y.right.parent = y
            self.__swap(node, y)
            y.left = node.left
            y.left.parent = y
            return

    def __swap(self, u, v) -> None:
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent
        return


def predecessor(node) -> TreeNode:
    if node.left is not None:
        return maximum(node.left)
    p = node.parent
    while p is not None and p.left == node:
        node = p
        p = p.parent
    return p


def minimum(node) -> TreeNode:
    while node.left is not None:
        node = node.left
    return node


def maximum(node) -> TreeNode:
    while node.right is not None:
        node = node.right
    return node


def successor(node) -> TreeNode:
    if node.right is not None:
        return minimum(node.right)
    p = node.parent
    while p is not None and p.right == node:
        node = p
        p = p.parent
    return p


def print_in_order(tree) -> None:
    def in_order(node):
        if node is None:
            return
        in_order(node.left)
        print(node.data, end=' ')
        in_order(node.right)

    in_order(tree.root)
    print()


def print_pre_order(tree):
    def pre_order(node):
        if node is None:
            return
        print(node.data, end=' ')
        pre_order(node.left)
        pre_order(node.right)

    pre_order(tree.root)
    print()


def post_order_walk(self) -> None:
    def post_order(node):
        if node is None:
            return
        post_order(node.right)
        print(node.data, end=' ')
        post_order(node.left)

    post_order(self.root)
    print()


if __name__ == "__main__":
    values_ = [6, 4, 8, 2, 5, 7, 9, 1, 3]
    nodes = []

    tree_ = BinaryTree(values_)
    print_in_order(tree_)

    tree_.remove(tree_.root)
    print_pre_order(tree_)
