#meant for findiong the largest amount of water that can be held between many different heights

def container_with_most_water(heights):

    left, right, area = 0, len(heights) - 1, 0

    while left < right:
        if heights[left] < heights[right]:
            height = heights[left]
            index = left
            area = max(area, (right - left) * (height))
            left += 1
        else:
            height = heights[right]
            index = right
            area = max(area, (right - left) * (height))
            right -= 1

    return area

#Testing#

print(container_with_most_water([1,8,6,2,5,4,8,3,7])) #Should be 49
print(container_with_most_water([4,3,2,1,4])) #Should be 16
    

# Logic behind the algorithm. 
# We initially set the left index to 0 and the right index to the last index in the list of heights. We also initialize the area to 0
# We then begin a while loop which has the end condition of "left >= right" which makes sense as this is when the 2 indexes will meet
# Inside of the while loop, there are 2 main conditionals.
# The first conditional checks to see which height is greater between the 2 indexes. 
# If the left height is greater, than the height index is set to the left index and the height is set to the value of the height at the left index (height[left])
# The opposite occurs if height[right] >= height[left]
# The largest area so far is then determined 
# Then the incrementing of the index occurs (up 1 if we are on the left index, down 1 if we are on the right index)
# After this has been done for the entirety of the loop, the area is finally returned. 