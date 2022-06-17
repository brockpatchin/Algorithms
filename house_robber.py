# Leetcode 198

# DP problem. Basic logic is to optimize choice following the recurrence Opt(n) = max(Opt(n-1), nums[n] + Opt(n-2))
# bottom up approach using memoization

def rob(nums):
    # init memo array with first nums value
    memo = [nums[0]]
    # iterate
    for i in range(1, len(nums)):
        # edge case where nums[i-2] returns nums[-1] (hacky solution to problem, probably more elegant way of handling it)
        if i < 2:
            memo.append(max(memo[i-1], nums[i]))
        # actual recurrence
        else:
            memo.append(max(memo[i-1], nums[i] + memo[i-2]))
    # return last value in memo array
    return memo[-1]
# Test Cases
print(rob([1,2,3,1])) # Expected 4
print(rob([2,7,9,3,1])) # Expected 12
    