def printSubSequences(op, ip, seq):
    if len(ip) == 0:
        seq.append("".join(op))
        return
    op1 = op + [ip[0]]
    ip = ip[1:]
    printSubSequences(op, ip, seq)
    printSubSequences(op1, ip, seq)

def main():
    ip = "321"
    seq = []
    printSubSequences([], ip, seq)
    print(*seq)
    print(len(seq))

if __name__ == "__main__":
    main()    