def findTreeDiameter(root):
    if root is None:
        return 0, 0
    leftHeight, leftDiameter = findTreeDiameter(root.left)
    rightHeight, rightDiameter = findTreeDiameter(root.right)
    treeHeight = max(leftHeight, rightHeight) + 1
    diameter = max(leftDiameter, rightDiameter, leftHeight + rightHeight)
    return treeHeight, diameter

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def main():
    global diameter
    tree = []
    for i in range(9):
        node = Node(i + 1)
        tree.append(node)
    for i in range(1, 10, 3):
        tree[i - 1].left = tree[i]
        tree[i - 1].right = tree[i + 1]
    height, diameter = findTreeDiameter(tree[0])
    print(diameter)
    
if __name__ == "__main__":
    main()