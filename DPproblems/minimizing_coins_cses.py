def find_minimum_coins(target, i, coins):
    if target < 0:
        return float("inf")
    if target == 0:
        return 0
    if i == len(coins):
        return float("inf")
    take = float("inf")
    if target >= coins[i]:
        take = 1 + find_minimum_coins(target - coins[i], i, coins)
    not_take = find_minimum_coins(target, i + 1, coins)
    return min(take, not_take)

def main():
    n, target = map(int, input().split())
    coins = [int(a) for a in input().split()]
    coins.sort()
    prev = [float("inf") for i in range(target + 1)]
    prev[0] = 0
    cur = [float("inf") for i in range(target + 1)]
    cur[0] = 0
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if coins[i - 1] <= j:
                cur[j] = min(1 + cur[j - coins[i - 1]], prev[j])
            else:
                cur[j] = prev[j]
        cur = prev.copy()
    print(prev[target] if prev[target] != float("inf") else -1)

if __name__ == "__main__":
    main()