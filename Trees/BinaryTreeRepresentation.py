class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

    def insert(self, val):
        if self.value:
            if val < self.value:
                if self.left is None:
                    self.left = Node(val)
                else:
                    self.left.insert(val)
            elif val > self.value:
                if self.right is None:
                    self.right = Node(val)
                else:
                    self.right.insert(val)
        else:
            self.value = val

#               RECURSIVE IMPLEMENTATION OF TRAVERSALS

# Time Complexity of Traversals is O(log(N))
# Space Complexity of Traversals is O(N)

    @staticmethod
    def preOrder(node):
        if node is None:
            return
        print(node.value)
        Node.preOrder(node.left)
        Node.preOrder(node.right)

    @staticmethod
    def inOrder(node):
        if node is None:
            return
        Node.inOrder(node.left)
        print(node.value)
        Node.inOrder(node.right)

    @staticmethod
    def postOrder(node):
        if node is None:
            return
        Node.postOrder(node.left)
        Node.postOrder(node.right)
        print(node.value)

# Time Complexity is O(N)
# Space Complexity is O(N)

    @staticmethod
    def levelOrder(root):
        if root is None:
            return
        queue = []
        queue.append(root)
        while len(queue) != 0:
            current = queue.pop(0)
            print(current.value)
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)

#                 ITERATIVE IMPLEMENTATION FOR TRAVERSALS
    @staticmethod
    # We will use STACK to do preOrder. In stack we follow LIFO.
    # So if we want to print left and then right, we have to first push right and then left into the stack.
    # Then only the top most element will be the left child.
    def preOrderIterative(root):
        stack = []
        stack.append(root)
        while len(stack) != 0:
            current = stack.pop()
            print(current.value)
            if current.right is not None:
                stack.append(current.right)
            if current.left is not None:
                stack.append(current.left)

    @staticmethod
    def inOrderTraversal(root):
        stack = []
        while True:
            if root is not None:
                stack.append(root)
                root = root.left
            else:
                if len(stack) == 0:
                    break
                root = stack.pop(0)
                print(root.value)
                root = root.right

    @staticmethod
    # Using 2 stacks
    def postOrderIterative(root):
        stack1, stack2 = [], []
        if root is None:
            return
        stack1.append(root)
        while len(stack1) != 0:
            root = stack1.pop()
            stack2.append(root)
            if root.left is not None:
                stack1.append(root.left)
            if root.right is not None:
                stack1.append(root.right)
        while len(stack2) != 0:
            print(stack2.pop().value)

    @staticmethod
    # using 1 stack
    def postOrderIterative2(root):
        current = root
        stack = []
        while current != None or len(stack) != 0:
            if current is not None:
                stack.append(current)
                current = current.left
            else:
                temp = stack[0].right
                if temp is None:
                    temp = stack.pop()
                    print(temp.value)
                else:
                    current = temp

    @staticmethod
    # all traversals using 1 stack
    def allTraversals(root):
        preorder = []
        inorder = []
        postorder = []
        stack = []
        stack.append([root, 1])
        while len(stack) != 0:
            current = stack[0]
            if current[1] == 1:
                preorder.append(current.value)
                stack[0][1] += 1
                if current.left is not None:
                    stack.append([current.left, 1])
            if current[1] == 2:
                inorder.append(current.value)
                current[1] += 1
                if current.right is not None:
                    stack.append([current.right, 1])
            if current[1] == 3:
                postorder.append(current.value)
                stack.pop(0)

    @staticmethod
    def maximumDepth(node):
        if node is None:
            return 0
        return 1 + max(Node.maximumDepth(node.left), Node.maximumDepth(node.right))

    @staticmethod
    def checkBalanced(node):
        if node is None:
            return 0
        leftHeight = Node.checkBalanced(node.left)
        if leftHeight == -1:
            return -1
        rightHeight = Node.checkBalanced(node.right)
        if rightHeight == -1:
            return -1
        if abs(rightHeight - leftHeight) > 1:
            return -1
        return max(leftHeight, rightHeight) + 1

    @staticmethod
    # Diameter - The maximum distance between any two nodes in the tree.
    def diameterBinaryTree(node):
        if node is None:
            return 0, 0
        leftHeight, leftDiameter = Node.diameterBinaryTree(node.left)
        rightHeight, rightDiameter = Node.diameterBinaryTree(node.right)
        return 1 + max(leftHeight, rightHeight), max(leftHeight + rightHeight, leftDiameter, rightDiameter)

    @staticmethod
    # Maximum Path sum
    # Approach
    # We find the sum of values from a node to another node by dfs.
    # Everytime we assume that particular node as a curving point, we add the left sum of that node and th right sum
    # of that node + that node's value.

    def maximumPathSum(node, maxPathSum = float("-inf")):
        if node is None:
            return 0
        leftSum = Node.maximumPathSum(node.left, maxPathSum)
        rightSum = Node.maximumPathSum(node.right, maxPathSum)
        if leftSum < 0:
            leftSum = 0
        if rightSum < 0:
            rightSum = 0
        maxPathSum = max(maxPathSum, leftSum + rightSum + node.val)
        return node.val + max(leftSum, rightSum)

    @staticmethod
    # Zig Zag traversal
    def zigzagTraversal(node):
        if node is None:
            return
        queue = []
        queue.append(node)
        zigzag = []
        flag = 0
        while True:
            level = []
            n = len(queue)
            if n == 0:
                break
            for i in range(n):
                current = queue.pop(0)
                level.append(current.value)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            if flag == 0:
                zigzag.append(level)
                flag = 1
            else:
                zigzag.append(level[::-1])
                flag = 0
        return zigzag

    @staticmethod
    # To check whether a node is leaf or not
    def isLeaf(node):
        if node.left is None and node.right is None:
            return True
        return False

root = Node(5)
root.insert(7)
root.insert(11)

Node.levelOrder(root)