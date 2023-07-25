class Solution:
    def isHappy(self, n: int) -> bool:
        nums = {}

        while n not in nums:
            nums[n] = 1
            total = 0
            while n > 0:
                digit = n % 10
                total += digit * digit
                n = (n - digit) / 10
            n = total

            if n == 1:
                return True
        
        return False
