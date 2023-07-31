class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        c1 = cost[len(cost) - 2]
        c2 = cost[len(cost) - 1]

        for i in range(len(cost) - 3, -1, -1):
            c1, c2 = min(cost[i] + c1, cost[i] + c2), c1

        return min(c1, c2)
