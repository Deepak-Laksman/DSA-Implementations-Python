def partitioning(string):
    partitions = []
    n = len(string)
    def recur(idx, partition):
        if idx == n:
            partitions.append(partition.copy())
            return
        for i in range(idx, n):
            if string[idx: i + 1] == string[idx: i + 1][::-1]:
                partition.append(string[idx: i + 1])
                recur(i + 1, partition)
                partition.pop()
    return partitions