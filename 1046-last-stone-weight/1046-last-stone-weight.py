class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            heaviest = heapq.heappop(stones)
            nextHeaviest = heapq.heappop(stones)
            if heaviest != nextHeaviest:
                heapq.heappush(stones, heaviest - nextHeaviest)

        if stones:
            return abs(stones[0])
        else:
            return 0
