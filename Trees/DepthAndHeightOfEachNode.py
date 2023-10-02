from collections import defaultdict

tree = []
depth = []
height = []
visited = []

def calc_depth_and_height(root, parent):
    global tree, depth
    for child in tree[root]:
        if child == parent:
            continue
        depth[child] = depth[root] + 1
        calc_depth_and_height(child, root)       
        height[root] = max(height[root], height[child] + 1) 


def main():
    global tree, depth, height
    tree = defaultdict(list)
    n, m = map(int, input().split())
    for _ in range(m):
        u, v = map(int, input().split())
        tree[u].append(v)
        tree[v].append(u)
    depth = [0] * (n + 1)
    height = [0] * (n + 1)
    calc_depth_and_height(1, 0)
    print(*depth)
    print(*height)
    
if __name__ == "__main__":
    main()