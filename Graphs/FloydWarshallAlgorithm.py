def floyd():
    n, m = map(int ,input().split())
    dist = [[float("inf")] * (n + 1) for i in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int ,input().split())
        dist[u][v] = w
    for i in range(n):
        dist[i][i] = 0
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dist[i][k] != float("inf") and dist[k][j] != float("inf"):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(dist[i][j], end = " ")
        print()

def main():
    floyd()

if __name__ == "__main__":
    main()