class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n

        n1, n2 = 2, 3

        for _ in range(n - 3):
            ways = n1 + n2
            n1 = n2
            n2 = ways

        return ways
