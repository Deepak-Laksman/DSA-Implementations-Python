import sys

def finalStandings(n, desiredStandings):
    desiredStandings.sort(key = lambda t : t[1])
    for i in range(n):
        desiredStandings[i][1] = i + 1
    return desiredStandings

def main():
    test_case = int(sys.stdin.readline())
    for tc in range(test_case):
        n = int(sys.stdin.readline())
        desiredStandings = []
        for _ in range(n):
            team , rank = map(str, sys.stdin.readline().split())
            rank = int(rank)
            desiredStandings.append([team, rank])
        print(*finalStandings(n, desiredStandings))

if __name__ == "__main__":
    main()
