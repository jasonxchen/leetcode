class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            if n not in counts:
                counts[n] = 1
            else:
                counts[n] += 1

        bucket = [[] for _ in range(len(nums))]
        for key, value in counts.items():
            bucket[-value].append(key)

        res = []
        for arr in bucket:
            k -= len(arr)
            res += arr
            if not k:
                break

        return res
