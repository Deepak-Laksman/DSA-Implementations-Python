def findSafeSpot(n, x, k, members):
    if n == 1:
        print(members[0])
        return
    members.pop((x + k - 1) % n)
    findSafeSpot(n - 1, (x + k - 1) % n, k, members)

def main():
    n, k = map(int, input().split())
    members = [(i + 1) for i in range(n)]
    findSafeSpot(n, 0, k, members)

if __name__ == "__main__":
    main()