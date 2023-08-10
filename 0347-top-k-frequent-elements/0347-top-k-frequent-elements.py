class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            if n not in counts:
                counts[n] = 1
            else:
                counts[n] += 1

        ordered = []
        for item in counts:
            for i, num in enumerate(ordered):
                if counts[item] < counts[num]:
                    ordered.insert(i, item)
                    break
            if item not in ordered:
                ordered.append(item)

        return ordered[-k:]
