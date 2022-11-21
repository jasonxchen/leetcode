class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1

        while start <= end:
            midpoint = (end + start) // 2
            if nums[midpoint] == target:
                return midpoint
            elif nums[midpoint] > target:
                end = midpoint - 1
            else:
                start = midpoint + 1
        return -1
        