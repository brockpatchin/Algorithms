def divisibleSumPairs(n, k, ar):
    counter = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
        	if (ar[i] + ar[j]) % k == 0:
       		    counter += 1
    return counter


print(divisibleSumPairs(6, 3, [1, 3, 2, 6, 1, 2]))


