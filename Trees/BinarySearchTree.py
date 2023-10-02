class BSTNode:
    def __init__(self, val = None):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

    def insert(self, val):
        if self.val is None:
            self.val = val
            return
        if val <= self.val:
            if self.left:
                self.left.insert(val)
            else:
                self.left = BSTNode(val)
        else:
            if self.right:
                self.right.insert(val)
            else:
                self.right = BSTNode(val)

    def search(self, val):
        if self.val is None:
            return False
        if self.val == val:
            return True
        if val < self.val:
            if self.left:
                self.left.search(val)
            else:
                return False
        if val > self.val:
            if self.right:
                self.right.search(val)
            else:
                return False

    def getMin(self):
        current = self
        while current is not None:
            current = current.left
        return current.val

    def getMax(self):
        current = self
        while current is not None:
            current = current.right
        return current.val

    def height(self):
        # -1 will be used to find height in terms of number of edges
        # 0 will be used to find height in terms of number of nodes
        if self is None:
            return -1
        leftHeight = self.left.height()
        rightHeight = self.right.height()
        return 1 + max(leftHeight, rightHeight)

    def preOrder(self):
        if self is None:
            return
        print(self.val)
        self.left.preOrder()
        self.right.preOrder()

    def inOrder(self):
        if self is None:
            return
        self.left.inOrder()
        print(self.val)
        self.right.inOrder()

    def postOrder(self):
        if self is None:
            return
        self.left.postOrder()
        self.right.postOrder()
        print(self.val)

    def levelOrder(self):
        if self is None:
            return
        queue = []
        queue.append(self)
        while len(queue) != 0:
            current = queue.pop(0)
            print(current.val, end = " ")
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        print()

    @staticmethod
    def findMin(node):
        if node is None:
            return
        temp = node
        while temp.left is not None:
            temp = temp.left
        return temp


    def delete(self, root, val):
        if root is None:
            return
        elif val < root.val:
            root.left = self.delete(root.left, val)
        elif val > root.val:
            root.right = self.delete(root.right, val)
        else:
            # Case 1: The node has no children
            if root.left is None and root.right is None:
                root = None
            # Case 2: The right child of node is None but left child is present
            elif root.left:
                temp = root
                root = root.left
                del temp
            elif root.right:
                temp = root
                root = root.right
                del temp
            else:
                # Finding minimum value in right subtree to replace it with root
                # We can also take the maximum value from left subtree
                temp = BSTNode.findMin(root.right)
                root.val = temp.val
                root.right = self.delete(root.right, temp.val)
            return root
    @staticmethod
    def find(root, val):
        if root is None:
            return
        if root.val == val:
            return root
        elif root.val < val:
            BSTNode.find(root.right, val)
        else:
            BSTNode.find(root.left, val)

    def getSuccessor(self, root, val):
        current = BSTNode.find(root, val)
        if current is None:
            return
        if current.right is not None:
            return BSTNode.findMin(current.right)
        else:
            successor = None
            ancestor = root
            while ancestor != current:
                if ancestor.val < current.val:
                    ancestor = ancestor.right
                else:
                    successor = ancestor
                    ancestor = ancestor.left
            return successor






# Check if a binary tree is binary search tree or not

def checkBST(node):
    pass

root = BSTNode(7)
node1 = BSTNode(11)
node2 = BSTNode(9)
root.left = node1
root.right = node2

print(checkBST(root))