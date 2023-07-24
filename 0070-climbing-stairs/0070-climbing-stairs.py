class Solution:
    def climbStairs(self, n: int) -> int:
        s1, s2, ways = 1, 1, 1

        for _ in range(n - 1):
            ways = s1 + s2
            temp = s1
            s1 += s2
            s2 = temp

        return ways
