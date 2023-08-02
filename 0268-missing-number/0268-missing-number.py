class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums) + 1):
            res += i
        for i in range(len(nums)):
            res -= nums[i]
        return res

        # res = nums[0]
        # for n in nums:
        #     # if n and n != 3:
        #     res ^= n
        # return res

# 0 1 2 3
# 0 1 - 3

# 00 0
# 01 1
# 10 2
# 11 3
