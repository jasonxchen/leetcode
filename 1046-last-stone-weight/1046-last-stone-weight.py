class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
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
