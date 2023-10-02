import sys

def maximumActivities(n, startTimes, endTimes):
    activities = list(zip(startTimes, endTimes))
    activities.sort(key = lambda t : t[1])
    activitiesCount = 1
    previous = 0
    for i in range(1, n):
        if activities[i][0] >= activities[previous][1]: 
            activitiesCount += 1
            previous = i
        i += 1
    return activitiesCount

def main():
    n = int(sys.stdin.readline())
    startTimes = [int(s) for s in sys.stdin.readline().split()]
    endTimes = [int(e) for e in sys.stdin.readline().split()]
    print(maximumActivities(n, startTimes, endTimes))

if __name__ == "__main__":
    main()