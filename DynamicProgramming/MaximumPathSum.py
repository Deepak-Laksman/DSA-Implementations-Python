maxSum = float("-inf")

def findMaximumPathSum(root):
    global maxSum
    if root is None:
        return 0
    leftSum = max(0, findMaximumPathSum(root.left))
    rightSum = max(0, findMaximumPathSum(root.right))
    maxSum = max(maxSum, leftSum + rightSum + root.val)
    return max(leftSum, rightSum) + root.val

def findMaxPathSumFromLeafToLeaf(root):
    global maxSum
    if root is None:
        return 0
    leftSum = findMaxPathSumFromLeafToLeaf(root.left)
    rightSum = findMaxPathSumFromLeafToLeaf(root.right)
    temp = max(leftSum, rightSum) + root.val
    maxSum = max(maxSum, temp, leftSum + rightSum + root.val)
    return temp

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def main():
    global maxSum
    tree = []
    for i in range(9):
        node = Node(i + 1)
        tree.append(node)
    for i in range(1, 10, 3):
        tree[i - 1].left = tree[i]
        tree[i - 1].right = tree[i + 1]
    tree[2].left = tree[3]
    tree[2].val = -100
    tree[8].val = -1
    temp = findMaximumPathSum(tree[8])
    print(maxSum)
    
if __name__ == "__main__":
    main()