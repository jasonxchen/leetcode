class Solution:
    def hammingWeight(self, n: int) -> int:
        total = 0

        while n:
            if n % 2 == 1:
                total += 1
            n = n >> 1

        return total
