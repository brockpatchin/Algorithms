# Solution for Leetcode 338 Counting Bits
# Logic for this question is similar to all other binary questions. 
# I created a powers array and used this due to the pattern that I noticed with the bits. 
# For each previous power, you add a new 1 infront of the binary string. 
# Example Below
# 0000   1000
# 0001   1001
# 0010   1010
# 0011   1011
# 0100   1100
# ............
# As you can see, for each subsequent iteration, you have the same number of bits for each accompanying binary string, but you change the parity of the first bit. 

# I employ the above logic for this
# Time and Space Complexities are odd for this question
# Time should be O(n)
# Space should be O(n + lgn) == O(n) (output array)


def countBits(n):
    # init powers array
    powers = [1]
    # fills an array with the powers of 2 all the way up to n
    while powers[-1] <= n:
        powers.append(powers[-1] * 2)
    # removes the last element to account for the above logic of changing the parity of the first bit (for 8 --> 16, there are 8 numbers with a 0 as the first bit and 8 with 1 as the first bit)
    powers.pop(-1)
    # init output array with 0
    output = [0]
    # logic of finding the pattern of adding 1 due to parity change for leading bit
    for i in range(len(powers)):
        for j in range(powers[i]):
            output.append(1 + output[len(output) - powers[i]])
            # stops when we arrive at n
            if len(output) == n + 1:
                break
    # returns output
    return output

print(countBits(2))
print(countBits(5))
        