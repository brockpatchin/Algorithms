# Leetcode 120
# DP question (done in place top-down)
# Logic is to optimize top-down using values from above
# At end, choose min from last row

# Complexities
# Time: O(n^2)
# Space: O(1)

def minimumTotal(triangle):
    # iterate
    for i in range(1, len(triangle)):
        # iterate
        for x in range(len(triangle[i])):
            # if we are at left edge of triangle
            if x == 0:
                # find only value
                triangle[i][x] += triangle[i-1][x]
            # if we are at right edge of triangle
            elif x == len(triangle[i]) - 1:
                # find only values
                triangle[i][x] += triangle[i-1][x-1]
            # if we are somewhere in middle
            else:
                # find min value
                triangle[i][x] += min(triangle[i-1][x], triangle[i-1][x-1])
    # return min of last row
    return min(triangle[-1])        

print(minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])) # Expected 11
print(minimumTotal([[-10]])) # Expected -10