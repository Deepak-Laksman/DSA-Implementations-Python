# inorder, postorder, preorder are depth first traversals

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)

def preorder(root):
    if root is None:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)

def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val)

from audioop import reverse
from cmath import inf
from collections import deque
from lib2to3.pytree import Node
from tabnanny import check

# level order is breadth first traversal

def levelOrder(root):
    if root is None:
        return
    queue = deque()
    queue.append(root)
    while len(queue):
        current = queue.popleft()
        print(current.val)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

def inorderIter(root):
    if root is None:
        return
    stack = deque()
    while True:
        if root is not None:
            stack.appendleft(root)
            root = root.left
        else:
            if len(stack) == 0:
                break
            root = stack.popleft()
            print(root.val, end = " ")
            root = root.right

def preorderIter(root):
    if root is None:
        return
    stack = deque()
    stack.append(root)
    while  len(stack):
        current = stack.popleft()
        print(current.val)
        if current.right:
            stack.appendleft(current.right)
        if current.left:
            stack.appendleft(current.left)

def postorderIter(root):
    if root is None:
        return
    stack1, stack2 = deque(), deque()
    stack1.appendleft(root)
    while len(stack1):
        current = stack1.popleft()
        stack2.appendleft(current.val)
        if current.left:
            stack1.appendleft(current.left)
        if current.right:
            stack1.appendleft(current.right)
    while len(stack2):
        print(stack2.popleft())

def postorder1stack(root):
    if root is None:
        return
    stack = []
    while root is not None or len(stack):
        if root is not None:
            stack.append(root)
            root = root.left
        else:
            temp = stack[-1].right
            if temp is None:
                temp = stack.pop()
                print(temp.val)
                while len(stack) and temp == stack[-1].right:
                    temp = stack.pop()
                    print(temp.val)
            else:
                root = temp
    print(*stack)

def allTraversals(root):
    stack = []
    stack.append((root, 1))
    preorder, inorder, postorder = [], [], []
    while len(stack):
        node, value = stack.pop()
        if value == 1:
            preorder.append(node.val)
            stack.append((node, value + 1))
            if node.left:
                stack.append((node.left, 1))
        elif value == 2:
            inorder.append(node.val)
            stack.append((node, value + 1))
            if node.right:
                stack.append((node.right, 1))
        else:
            postorder.append(node.val)
    print(*preorder)
    print(*inorder)
    print(*postorder)

def checkBalanced(root):
    if root is None:
        return 0
    lh = checkBalanced(root.left)
    if lh == -1:
        return -1
    rh = checkBalanced(root.right)
    if rh == -1:
        return -1
    if abs(lh - rh) > 1:
        return -1
    return 1 + max(lh, rh)

def diameter(root):
    if root is None:
        return 0, 0
    lh, ld = diameter(root.left)
    rh, rd =  diameter(root.right)
    return 1 + max(lh, rh), max(lh + rh, ld, rd)

def max_path_sum(root, ans):
    if root is None:
        return 0
    lv = max(0, max_path_sum(root.left, ans))
    rv = max(0, max_path_sum(root.right, ans))
    ans[0] = max(ans[0], root.val + lv + rv)
    return root.val + max(lv, rv)

def isLeaf(root):
    if root.left is None and root.right is None:
        return True
    return False

def left_traversal(root):
    if root is None:
        return
    left = []
    queue = deque()
    queue.append(root)
    while len(queue):
        cur = queue.popleft()
        if isLeaf(cur):
            continue
        left.append(cur.val)
        if cur.left:
            queue.append(cur.left)
        elif cur.right:
            queue.append(cur.right)
    return left

def right_traversal(root):
    if root is None:
        return
    right = []
    queue = deque()
    queue.append(root)
    while len(queue):
        cur = queue.popleft()
        if isLeaf(cur):
            continue
        right.append(cur.val)
        if cur.right:
            queue.append(cur.right)
        elif cur.left:
            queue.append(cur.left)
    return right

def leaf_traversal(root, leaf):
    if root is None:
        return []
    if isLeaf(root):
        return leaf + [root.val]
    leaf = leaf_traversal(root.left, leaf)
    leaf = leaf_traversal(root.right, leaf)
    return leaf

def boundary_traversal(root):
    if root is None:
        return []
    if root.left is None and root.right is None:
        return [root.val]
    left_nodes = left_traversal(root.left)
    right_nodes = right_traversal(root.right)
    leaf_nodes = leaf_traversal(root, [])
    return  [root.val] + left_nodes + leaf_nodes + right_nodes[::-1] 

from heapq import heappush, heappop
def vertical_order(root):
    if root is None:
        return []
    stack = [(0, 0, root)]
    heap = []
    while len(stack):
        row, col, root = stack.pop()
        heappush(heap, (col, row, root.val))
        if root.right:
            stack.append((row + 1, col + 1, root.right))
        if root.left:
            stack.append((row + 1, col - 1, root.left))
    start_col = heap[0][0]
    order = []
    while heap:
        col, row, value = heappop(heap)
        if len(order) < col - start_col + 1:
            order.append([])
        order[col - start_col].append(value)
    return order

def top_view(root):
    if root is None:
        return 
    hashmap = {}
    queue = []
    queue.append((0, root))
    while len(queue):
        col, root = queue.pop(0)
        if col not in hashmap:
            hashmap[col] = root.val
        if root.left:
            queue.append((col - 1, root.left))
        if root.right:
            queue.append((col + 1, root.right))
    view = []
    for col in sorted(hashmap.keys()):
        view.append(hashmap[col])
    return view

def bottom_view(root):
    if root is None:
        return 
    hashmap = {}
    queue = []
    queue.append((0, root))
    while len(queue):
        col, root = queue.pop(0)
        hashmap[col] = root.val
        if root.left:
            queue.append((col - 1, root.left))
        if root.right:
            queue.append((col + 1, root.right))
    view = []
    for col in sorted(hashmap.keys()):
        view.append(hashmap[col])
    return view

def left_view(root):
    if root is None:
        return
    levels = set()
    left = []
    stack = [(0, root)]
    while len(stack):
        level, root = stack.pop()
        if level not in levels:
            left.append(root.val)
            levels.add(level)
        if root.right:
            stack.append((level + 1, root.right))
        if root.left:
            stack.append((level + 1, root.left))
    return left

def right_view(root):
    if root is None:
        return
    levels = set()
    right = []
    stack = [(0, root)]
    while len(stack):
        level, root = stack.pop()
        if level not in levels:
            right.append(root.val)
        if root.left:
            stack.append((level + 1, root.left))
        if root.right:
            stack.append((level + 1, root.right))
    return right

def check_symmetric(root):
    if root is None:
        return True
    stack = [(root.left, root.right)]
    while len(stack):
        left, right = stack.pop()
        if left is None and right is None:
            continue
        elif (left is None or right is None):
            return False
        elif left.val != right.val:
            return False
        else:
            stack.append((left.left, right.right))
            stack.append((left.right, right.left))
    return True

# too much space
def root_to_node(root, node):
    if root.left is None and root.right is None:
        return []
    stack = [(root, [])]
    while len(stack):
        root, path = stack.pop()
        if root.val == node.val:
            return path + [root.val]
        if root.left:
            stack.append((root.left, path + [root.val]))
        if root.right:
            stack.append((root.right, path + [root.val]))
    return []

# less space compared to it
def root_to_node_recur(root, node):
    path = []
    def find_path(root, node):
        nonlocal path
        if root is None:
            return False
        path.append(root.val)
        if root.val == node.val:
            return True
        if find_path(root.left, node) or find_path(root.right, node):
            return True
        path.remove(root.val)
        return False
    find_path(root, node)
    return path

def lowestCommonAncestor(self, root, p, q):
    if root is None or root == p or root == q:
        return root
    left, right = lowestCommonAncestor(root.left, p, q), lowestCommonAncestor(root.right, p, q)
    if left is None:
        return right
    elif right is None:
        return left
    else:
        return root

def maximum_width_of_binary_tree(root):
        if root is None:
            return 0
        queue = deque()
        queue.append((0, root))
        max_width = 0
        while True:
            if len(queue) == 0:
                break
            max_width = max(max_width, queue[-1][0] - queue[0][0] + 1)            
            for _ in range(len(queue)):
                par, root = queue.popleft()
                if root.left:
                    queue.append((par * 2 + 1, root.left))
                if root.right:
                    queue.append((par * 2 + 2, root.right))
        return max_width
        
def children_sum_property(root):
    if root is None:
        return
    def dfs(root):
        if root is None:
            return 
        child = 0
        if root.left:
            child += root.left.val
        if root.right:
            child += root.right.val
        if child >= root.val:
            root.val = child
        else:
            if root.left:
                root.left.val = child
            elif root.right:
                root.right.val = child
        dfs(root.left)
        dfs(root.right)
        total = 0
        if root.left:
            total += root.left.val
        if root.right:
            total += root.right.val
        if root.left or root.right:
            root.val = total
    dfs(root)
    queue = [(root)]
    while len(queue):
        cur = queue.pop(0)
        print(cur.val, end = " ")
        if cur.left:
            queue.append(cur.left)
        if cur.right:
            queue.append(cur.right)

def nodes_with_distance_k_from_target(root, target, k):
    queue = deque()
    parent = {}
    queue.append((root, root))
    
    while len(queue):
        cur, par = queue.popleft()
        parent[cur] = par
        if cur.left:
            queue.append((cur.left, cur))
        if cur.right:
            queue.append((cur.right, cur))
    
    visited = set()
    queue.clear()
    queue.append((0, root))
    values = []

    while len(queue):
        dis, node = queue.popleft()
        visited.add(node)
        if dis == k:
            values.append(node.val)
        if node.left and node.left not in visited:
            queue.append((dis + 1, node.left))
        if node.right and node.right not in visited:
            queue.append((dis + 1, node.right))
        if parent[node] and parent[node] not in visited:
            queue.append((dis + 1, parent[node]))
    
    return values

def minimum_time_to_burn_a_tree_from_given_node(root, node):
    parent = {}
    queue = deque()
    queue.append((root, root))
    
    while len(queue):
        cur, par = queue.popleft()
        parent[cur] = par
        if cur.left:
            queue.append((cur.left, cur))
        if cur.right:
            queue.append((cur.right, cur))
    
    time = 0
    queue.clear()
    visited = set()
    queue.append(node)

    while True:
        if len(queue) == 0:
            break
        for _ in range(len(queue)):
            node = queue.popleft()
            visited.add(node)
            if node.left and node.left not in visited:
                queue.append(node.left)
            if node.right and node.right not in visited:
                queue.append(node.right)
            if parent[node] and parent[node] not in visited:
                queue.append(parent[node])
        time += 1
    return time

def left_height(root):
    height = 0
    while root:
        height += 1
        root = root.left
    return height

def right_height(root):
    height = 0
    while root:
        height += 1
        root = root.right
    return height

# TC -> O(log(N) ** 2)
def count_nodes(root):
    if root is None:
        return 0
    lh = left_height(root)
    rh = right_height(root)
    if lh == rh:
        return (1 << lh) - 1
    return 1 + count_nodes(root.left) + count_nodes(root.right)


# contruct binary tree from preorder and inorder traversal
def contruct_unique_binary_tree_pre(inorder, preorder):
    inmap = {}
    for i in range(len(inorder)):
        inmap[inorder[i]] = i
    root = build_tree_pre(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1, inmap)
    return root

def build_tree_pre(preorder, pre_start, pre_end, inorder, in_start, in_end, inmap):
    if pre_start > pre_end or in_start > in_end:
        return 
    root = node(preorder[pre_start])
    in_root = inmap[root.val]
    nums_left = in_start - in_root
    root.left = build_tree_pre(preorder, pre_start + 1, pre_start + nums_left, inorder, in_start, in_start - in_root, inmap)
    root.right = build_tree_pre(preorder, pre_start + nums_left + 1, pre_end, inorder, in_root + 1, in_end, inmap)
    return root

# contruct binary tree from postorder and inorder traversal
def construct_binary_tree_post(inorder, postorder):
    inmap = {}
    for i in range(len(inorder)):
        inmap[inorder[i]] = i
    postorder.reverse()
    root = build_tree_post(postorder, 0, len(postorder) - 1, 0, len(inorder) - 1, inmap)
    return root

def build_tree_post(postorder, post_start, post_end, in_start, in_end, inmap):
    if post_start > post_end or in_start > in_end:
        return
    root = node(postorder[post_start])
    in_root = inmap[root.val]
    nums_right = in_end - in_root
    root.left = build_tree_post(postorder, post_start + nums_right + 1, post_end, in_start, in_root - 1, inmap)
    root.right = build_tree_post(postorder, post_start + 1, post_start + nums_right, in_root + 1, in_end, inmap)
    return root

def morris_traversal(root):
    # for inorder
    inorder = []
    cur = root
    while cur:
        if cur.left is None:
            inorder.append(cur.val)
            cur = cur.right
        else:
            prev = cur.left
            while prev.right and prev.right != cur:
                prev = prev.right
            if prev.right is None:
                prev.right = cur
                cur = cur.left
            else:
                prev.right = None
                inorder.append(cur.val)
                cur = cur.right
    # for preorder
    preorder = []
    cur = root
    while cur:
        if cur.left is None:
            preorder.append(cur.val)
            cur = cur.right
        else:
            prev = cur.left
            while prev.right and prev.right != cur:
                prev = prev.right
            if prev.right is None:
                prev.right = cur
                preorder.append(cur.val)
                cur = cur.left
            else:
                prev.right = None
                cur = cur.right
    return inorder, preorder

def flatten_binary_tree_to_linkedlist(root):
    # right left root traversal or reverse postorder
    # time is O(N), space is O(N)
    stack = deque()
    stack.append(root)
    while len(stack):
        cur = stack.pop()
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)
        if len(stack):
            cur.right = stack[-1]
        cur.left = None

def flatten_using_morris_traversal(root):
    cur = root
    while cur:
        if cur.left:
            prev = cur.left
            while prev.right:
                prev = prev.right
            prev.right = cur.right
            cur.right = cur.left
            cur.left = None
        cur = cur.right
    return root

def ceil_in_bst(root, val):
    if root is None:
        return
    ceill = float("inf")
    ceil_node = None
    while root:
        if root.val > val:
            if root.val < ceill:
                ceill = root.val
                ceil_node = root
            root = root.left
        else:
            root = root.right
    return ceil_node

def floor_in_bst(root, val):
    if root is None:
        return 
    floor = float("-inf")
    floor_node = None
    while root:
        if root.val < val:
            if root.val > floor:
                floor = root.val
                floor_node = root
            root = root.right
        else:
            root = root.left
    return floor_node

def search_in_bst(root, val):
    if root is None:
        return
    while root and root.val != val:
        if root.val > val:
            root = root.left
        else:
            root = root.right
    return root

def insert_node_in_bst(root, key):
    new_node = node(key)
    if root is None:
        return new_node
    cur = root
    while cur:
        if cur.val < key:
            if cur.right:
                cur = cur.right
            else:
                cur.right = new_node
                return root
        else:
            if cur.left:
                cur = cur.left
            else:
                cur.left = new_node
                return root

# delete node in a bst
def find_left_max(root):
    while root.right:
        root = root.right
    return root

def delete_helper(root):
    if root.left is None:
        return root.right
    if root.right is None:
        return root.left
    temp = root
    right_node = root.right
    left_node = find_left_max(root.left)
    left_node.right = right_node
    temp.right = None
    return root.left

def delete_node_in_a_bst(root, key):
    if root is None:
        return
    if root.val == key:
        return delete_helper(root)
    dummy = root
    while root:
        if root.val < key:
            if root.right and root.right.val == key:
                root.right = delete_helper(root.right)
                break
            else:
                root = root.right
        else:
            if root.left and root.left.val == key:
                root.left = delete_helper(root.left)
                break
            else:
                root = root.left
    return dummy

def kth_smallest_in_bst(root, k):
    # using morris traversal
    while root:
        if root.left is None:
            k -= 1
            if k == 0:
                return root.val
            root = root.right
        else:
            prev = root.left
            while prev.right and prev.right != root:
                prev = prev.right
            if prev.right is None:
                prev.right = root
                root = root.left
            else:
                prev.right = None
                k -= 1
                if k == 0:
                    return root.val
                root = root.right

def validate_bst(root):
    def dfs(root, lower = -inf, upper = inf):
        if root is None:
            return True
        if lower >= root.val or upper <= root.val:
            return False
        return dfs(root.left, lower, root.val) and dfs(root.right, root.val, upper)
    return dfs(root)

def lca_in_bst(root, p, q):
    if p.val > q.val:
        while root:
            if q.val <= root.val <= p.val:
                return root
            elif q.val > root.val:
                root = root.right
            elif p.val < root.val:
                root = root.left
    else:
        while root:
            if p.val <= root.val <= q.val:
                return root
            elif p.val > root.val:
                root = root.right
            elif q.val < root.val:
                root = root.left
    return 

def construct_bst_from_preorder(preorder):
    idx = 0
    n = len(preorder)
    def build(upper = inf):
        nonlocal n, idx, preorder
        if idx < n:
            val = preorder[idx]
            if val <= upper:
                idx += 1
                root = node(val)
                root.left = build(val)
                root.right = build(upper)
                return root
    return build()

def inorder_successor(root, key):
    successor = None 
    while root:
        if root.val > key:
            successor = root
            root = root.left
        else:
            root = root.right
    return successor

def inorder_predecessor(root, key):
    predecessor = None
    while root:
        if root.val < key:
            predecessor = root
            root = root.right
        else:
            root = root.left
    return predecessor

class BSTIterator:

    def __init__(self, root, isReverse):
        self.reverse = isReverse
        self.stack = deque()
        self.pushAll(root)

    def next(self):
        node = self.stack.pop()
        if self.reverse:
            self.pushAll(node.left)
        else:
            self.pushAll(node.right)
        return node.val

    def hasNext(self):
        if len(self.stack):
            return True
        return False

    def pushAll(self, root):
        while root:
            self.stack.append(root)
            if self.reverse:
                node = node.right
            else:
                node = node.left

def two_sum_in_bst(root, target):
    l, r = BSTIterator(root, False), BSTIterator(root, True)
    i, j = l.next(), r.next()
    while i < j:
        if i + j == target:
            return True
        elif i + j < target:
            i = l.next()
        else:
            j = r.next()
    return False
    
def recover_bst():
    pass

def largest_bst():
    pass

# Test Code

class node:
    def __init__(self, val, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

node1 = node(1)
node2 = node(2)
node3 = node(3)
node4 = node(4)
node5 = node(5)
node6 = node(6)
node7 = node(7)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
ans = [float("-inf")]
print(count_nodes(node1))