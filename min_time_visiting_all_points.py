# Leetcode 1266
# Given a set of points, find the min time it takes to get each consecutive point
# time is given as (1 for 1 horizontal, 1 for 1 vertical, and 1 for sqrt 2 diagonal (1 vertical and 1 horizontal at the same time))
# The given conditions make the question as simple as finding the larger of the x-distance and y-distance

# Complexity
# Time is O(n)
# Space is O(1)

def minTimeToVisitAllPoints(points):
    total = 0
    for i in range(len(points) - 1):    
        # finds maximum between y-distance and x-distance
        total += max(abs(points[i][0] - points[i+1][0]), abs(points[i][1] - points[i+1][1]))
    return total
        
print(minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]])) # Expected 7
print(minTimeToVisitAllPoints([[3,2],[-2,2]])) # Expected 5