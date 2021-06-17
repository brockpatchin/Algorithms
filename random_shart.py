def merge(nums1, m, nums2, n):       
    if nums2 == []:
        return nums1
    elif nums1 == []:
        return nums2

    #edge case
    elif m == 1 and n == 1:
        nums1[1] = max(nums1[0], nums2[0])
        nums1[0] = min(nums1[0], nums2[0])
        return nums1

    ptr = 0
    catcher = 0
    for i in range(m + n):
        if (nums1[i] >= nums2[ptr] and catcher == 0) or nums1[i] == 0:
            nums1.insert(i, nums2[ptr])
            nums1.pop()
            if ptr + 1 == n:
            	catcher = 1
            if ptr + 1 != n:
                ptr += 1

    return nums1

print(merge([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3))

print(merge([2, 0], 1, [1], 1))

print(merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))

