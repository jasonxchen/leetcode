class Solution:
    def hammingWeight(self, n: int) -> int:
        # total = 0
        # while n:
        #     total += n % 2
        #     n >>= 1

        # return total

        # 'skips' 0s
        total = 0
        while n:
            n &= n - 1
            total += 1

        return total
