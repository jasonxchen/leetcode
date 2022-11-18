class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i, num in enumerate(nums):
            if target - num not in nums_dict:
                nums_dict[num] = i
            else:
                return [i, nums_dict[target - num]]
