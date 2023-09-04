class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        bucket = [[] for _ in range(len(nums))]
        res = []

        for n in nums:
            counts[n] = counts.get(n, 0) + 1

        for key, value in counts.items():
            bucket[-value].append(key)

        for arr in bucket:
            res += arr
            if len(res) == k:
                return res
