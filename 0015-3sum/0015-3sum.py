class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums) #
        triplets = []

        for i, num in enumerate(nums):
            if i == 0 or num != nums[i - 1]:
                l = i + 1
                r = len(nums) - 1
                while l < r:
                    if num + nums[l] + nums[r] < 0:
                        l += 1
                    elif num + nums[l] + nums[r] > 0:
                        r -= 1
                    else:
                        triplets.append([num, nums[l], nums[r]])
                        l += 1
                        while nums[l] == nums[l -1] and l < r: #
                            l += 1

        return triplets
