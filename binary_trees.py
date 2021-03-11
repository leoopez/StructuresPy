class TreeNode:
    def __init__(self, val = 0, parent = None, left = None, right = None):
        self._height = 1;
        self.val = int(val)
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        return str(self.val)

class Tree:
    def __init__(self, root= None):
        self.root = root

    def InOrderTreeWalk(self):
        def InOrder(node):
            if(node is None):
                return
            InOrder(node.left)
            print(node.val, end = " ")
            InOrder(node.right)
        
        InOrder(self.root)
        print()
    

    def PreOrderTreeWalk(self):
        def PreOrder(node):
            if(node is None):
                return
            print(node.val, end =' ')
            PreOrder(node.left) 
            PreOrder(node.right)
        PreOrder(self.root)
        print()

    def PostOrderTreeWalk(self):
        def PostOrder(node):
            if(node is None):
                return
            PostOrder(node.right)
            print(node.val, end =' ')
            PostOrder(node.left)

        PostOrder(self.root)
        print()
    
    def TreeSearch(self,key):
        def NodeSearch(node, k):
            if node is None or node.val == k:
                return node
            if node.val > key:
                return NodeSearch(node.left, k)
            else:
                return NodeSearch(node.right,k)
        return NodeSearch(self.root, key)

    def Minimum(self):
        node = self.root
        while node.left is not None:
            node = node.left
        return node

    def Maximum(self):
        node = self.root
        while node.right is not None:
            node = node.right
        return node
    
    def Successor(self,key):
        node = self.TreeSearch(key)
        if node.right is not None:
            return node.right
        p = node.parent
        while p is not None and p.right == node:
            node = p
            p = p.parent
        return p

    def Predecessor(self,key):
        node = self.TreeSearch(key)
        if node.left is not None:
            return node.left
        p = node.parent
        while p is not None and p.left == node:
            node = p
            p = p.parent
        return p
    def Insert(self, value):
        node = TreeNode(value)

        if self.root is None:
            self.root = node
            return

        par = TreeNode()
        pos = self.root

        while pos is not None:
            par = pos
            if pos.val < value:
                pos = pos.right
            else:
                pos = pos.left

        if par.val < value:
            par.right = node
        else:
            par.left = node
        node.parent = par

    def Delete(self,key):
        node = self.TreeSearch(key)
        def replace(u,v):
            if u.parent is None:
                self.root = v
            elif u == u.parent.left:
                u.parent.left = v
            else:
                u.parent.right = v
            if v is not None:
                v.parent = u.parent
        
        if node.left is None:
            replace(node, node.right)
        elif node.right is None:
            replace(node, node.left)
        else:
            y = self.Successor(node.val)
            if y.parent is not node:
                replace(y,y.right)
                y.right = node.right
                y.right.parent = y
            replace(node, y)
            y.left = node.left
            y.left.parent = y

if __name__ == '__main__':
    

    nodes = [6,4,9,2,5,8,10,1,3]
    tree = Tree()
    for i in nodes:
        tree.Insert(i)

    tree.InOrderTreeWalk()
    tree.PreOrderTreeWalk()
    tree.PostOrderTreeWalk()
    print("node search:", tree.TreeSearch(3))
    print("minimum node:", tree.Minimum())
    print("maximum node:", tree.Maximum())
    print("successor:",tree.Successor(3))
    print("predecessor:",tree.Predecessor(5))

    tree.Delete(5)
    tree.Delete(6)
    tree.InOrderTreeWalk()
