# Hamming Weight Question from Leetcode (191. Number of 1 Bits)
# The logic employed for this question is to virtually convert the number to binary 
# The way that this is done is by finding the largest power of 2 <= to our actual number. From here, we iterate through each power of 2 decrementing when necessary
# This will find the total number of 1's due to the fact that the number is virtually being converted to binary
# Time complexity is lgn

def hammingWeight(n):
    # initalize array for powers of 2 with 2^0
    powers = [1]
    # fill previously made array with powers of 2 all the way up to n
    while powers[-1] * 2 <= n:
        powers.append(powers[-1] * 2)
    # initalize output and temp values
    output = 0
    temp = n
    # go through the array containing the powers of 2 subtracting the largest power of 2 when possible.
    # at each successful subtraction, increment the output as a 1 was found in the binary representation of the given input integer
    for i in range(len(powers) - 1, -1, -1):
        if temp >= powers[i]:
            temp -= powers[i]
            output += 1
    # return output which contains the total number of 1's
    return output

# Test Cases #
print(hammingWeight(0b00000000000000000000000000001011))
print(hammingWeight(0b00000000000000000000000010000000))
print(hammingWeight(0b11111111111111111111111111111101))
# End of Test Cases #