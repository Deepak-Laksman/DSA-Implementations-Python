# The game of nim is a game where 2 players play and each player can remove atleast one stone from n piles of stone.
# We should determine the winner before playing the game itself.
# One player will play first.
# So if its a winning state then that player will win, if its a losing state then the other player will win.
# A winning state is position from where we can go to a losing state.
# But from a losing state we cannot go to a losing state again.
# The xor operation has a very good use here.
# The total xor of all the number of stones in each pile will give either a non-zero value or a zero value.
# If its zero, then its a losing state for the first player because if he removes any number of stones from any pile,
# he will make the xor sum a non-zero value, which is a winning state.
# And wise versa

def findWinner(N, array):
    ans = 0
    for i in range(N):
        ans ^= array[i]
    if ans > 0:
        return False
    return True

# Grundy Numbers

# If we are given a value of n, and a set of rules like we are allowed to remove a certain number of values or
# divide the value n by a certain number of values, then we can calculate the grundy value by using the concept of mex.
# Mex is the minimum number that is not found in the set.
# For Example, if we are given a number n, and we can subtract 1, 2 or 3 from n until n becomes zero, find the winner.
# 1st player subtracts first.
# Now, if 1st player takes 1, n becomes n - 1, ....
# Grundy(n) = Mex(n - 1, n - 2, n - 3) = 0 (if n > 3)
# if n = 3, then Grundy(3) = Mex(0, 1, 2) = 3
# if n = 2, then Grundy(2) = Mex(0, 1) = 2
# if n = 1, then Grundy(1) = Mex(0) = 1

print(3 ^ 0 ^ 1)