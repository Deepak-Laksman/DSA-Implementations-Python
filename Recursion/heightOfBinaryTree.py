def heightOfTree(root):
    if root is None:
        return 0
    return 1 + max(heightOfTree(root.left), heightOfTree(root.right))