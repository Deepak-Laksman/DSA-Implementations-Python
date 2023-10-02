def make_string(n, final, string):
    if n == 0:
        final.append(string)
        return
    if len(string) == 0 or string[len(string) - 1] != "B":
        make_string(n - 1, final, string + "A")
        make_string(n - 1, final, string + "B")
    else:
        make_string(n - 1, final, string + "A")

def main():
    n, m = map(int, input().split())
    final = []
    make_string(n, final, "")
    final.sort()
    if m > len(final):
        print("Not Possible")
    else:
        print(final[m - 1])

if __name__ == "__main__":
    main()