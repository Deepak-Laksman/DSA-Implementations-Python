def find_max_pages(target, i, price, pages, dp):
    if target <= 0 or i == len(price):
        return 0
    if dp[i][target] != -1:
        return dp[i][target]
    take = 0
    if target >= price[i]:
        take = max(pages[i] + find_max_pages(target - price[i], i + 1, price, pages, dp), find_max_pages(target, i + 1, price, pages, dp))
    not_take = find_max_pages(target, i + 1, price, pages, dp)
    dp[i][target] = max(take, not_take)
    return dp[i][target]

def main():
    n, capacity = map(int, input().split())
    price = [int(a) for a in input().split()]
    pages = [int(a) for a in input().split()]
    prev = [0 for i in range(capacity + 1)]
    cur = [0 for i in range(capacity + 1)]
    for i in range(1, capacity + 1):
        for j in range(n):
            cur[i] = prev[i]
            if price[j] <= i:
                cur[i] = max(cur[i], pages[j] + prev[i - price[j]])
        prev = cur
    print(prev[capacity])
    

if __name__ == "__main__":
    main()