class RedBlackNode:
    def __init__(self, data=None, parent=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
        self.color = 0

    def __str__(self):
        return str(self.data)


class RedBlackTree:
    def __init__(self, values=None):
        self.nil = RedBlackNode()
        self.root = self.nil

    def insert(self, node) -> None:
        pass

    def remove(self, node):
        pass

    def search(self, node):
        pass


if __name__ == '__main__':
    pass
