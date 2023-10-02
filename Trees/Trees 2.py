# Boundary Traversal

def isLeaf(node):
    if node.left is None and node.right is None:
        return True
    return False

def leftTraversal(node):
    if node is None:
        return []
    result = []
    queue = []
    queue.append(node)
    while len(queue) != 0:
        current = queue.pop(0)
        result.append(current.value)
        if current.left is not None and not isLeaf(current.left):
            queue.append(current.left)
        elif current.right is not None and not isLeaf(current.right):
            queue.append(current.right)
    return result

def rightTraversal(node):
    if node is None:
        return []
    queue = [node]
    result = []
    while len(queue) != 0:
        current = queue.pop(0)
        result.append(current.value)
        if current.right is not None and not isLeaf(current.right):
            queue.append(current.right)
        elif current.left is not None and not isLeaf(current.left):
            queue.append(current.left)
    result.pop(0)
    return result[::-1]

def leafTraversal(node, result):
    if isLeaf(node):
        result.append(node.value)
        return
    leafTraversal(node.left, result)

    leafTraversal(node.right, result)

def boundaryTraversal(node):
    left = leftTraversal(node)
    right = rightTraversal(node)
    leaves = []
    leafTraversal(node, leaves)
    answer = left + leaves + right
    return answer