import math
# Leetcode 279
# This question is a DP question similar to Coin Change (2-D)
# Basic Memoization structure 

# Complexities
# Time: O(n + sqrt(n))
# Space: O(n + sqrt(n))

def numSquares(n):
    # inits 2 lists, one for memoization and one for perfect square counter
    memo, ps = [0], []
    # iterate
    for i in range(1, n + 1):
        # Tests to see if i is perfect square
        if i == int(math.sqrt(i) + 0.5) ** 2:
            # if so, add to perfect square list
            ps.append(i)
        temp = 1000000 # large number
        # iterate through perfect square list (2d approach similar to iterating through list of coins in coin change)
        for x in range(len(ps)):
            # DP logic (bottom up)
            temp = min(temp, 1 + memo[i - ps[x]])
        #print(str(i) + " " + str(temp))
        # add newly found value to memo list
        memo.append(temp)
    # return last value from memo
    return memo[-1]        

print(numSquares(12)) # Expected 3
print(numSquares(13)) # Expected 2