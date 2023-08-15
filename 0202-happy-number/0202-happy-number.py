class Solution:
    def isHappy(self, n: int) -> bool:
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
        while n:
            total += (n % 10) ** 2
            n //= 10
        return total
