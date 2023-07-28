class Solution:
    def isHappy(self, n: int) -> bool:
        # nums = {}

        # while n not in nums:
        #     nums[n] = 1
        #     total = 0
        #     while n > 0:
        #         digit = n % 10
        #         total += digit * digit
        #         n = (n - digit) / 10
        #     n = total

        #     if n == 1:
        #         return True
        
        # return False

        slow = n
        fast = self.sumSquares(self.sumSquares(n))

        while fast != 1:
            slow = self.sumSquares(slow)
            fast = self.sumSquares(self.sumSquares(fast))
            if fast == slow:
                return False
        
        return True

    def sumSquares(self, n: int) -> int:
        total = 0
        while n > 0:
            total += (n % 10) ** 2
            n = n // 10
        return total
