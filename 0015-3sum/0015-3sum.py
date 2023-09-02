class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []

        for i, num in enumerate(nums):
            if i == 0 or num != nums[i - 1]:
                l, r = i + 1, len(nums) - 1
                while l < r:
                    three_sum = num + nums[l] + nums[r]
                    if three_sum < 0:
                        l += 1
                    elif three_sum > 0:
                        r -= 1
                    else:
                        triplets.append([num, nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while nums[l] == nums[l - 1] and l < r:
                            l += 1

        return triplets
