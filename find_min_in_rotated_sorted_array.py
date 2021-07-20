def findMin(nums):
    # Implements Unique Binary Search
    
    length = len(nums)
    
    # if length is 1, just return the only element
    if length == 1:
        return nums[0]
    
    # creates a right pointer and a left pointer starting at the beginning and the end of the list
    lp = 0
    rp = length - 1
    
    # no rotation #
    # if nums[right pointer] > nums[0] or the last element is greater than the first element, than this means that the array is sorted so we can just return the smallest element
    if nums[rp] > nums[0]:
        return nums[0]

    # while right pointer is less than left pointer
    while rp >= lp:
        # middle pointer is equal to the middle of lp and rp
        mp = lp + (rp - lp) / 2
        # if nums[mp] > than next element, than next element is smallest
        if nums[mp] > nums[mp + 1]:
            return nums[mp + 1]
        # conversely, if the element before nums[mp] is greater than nums[mp], that means that nums[mp] is min
        if nums[mp - 1] > nums[mp]:
            return nums[mp]
        # if the value at the middle pointer is greater than the first element, this means that the inflection point or where we switch from largest to smallest is to the left
        if nums[mp] > nums[0]:
            lp = mp + 1
        # conversely, if the above condition is not true, this means that the inflection points is to the left of the mid pointer
        else:
            rp = mp + 1

    # altogether, this problem can be solved with brute force (linear search) where the time complexity would be O(N), but implementing binary search drops the time complexity to O(log n).
    # in both cases, space complexity is O(1)
    
    
        
    