class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_area = min(height[l], height[r]) * (r - l)

        while l < r:
            # new_left = min(height[l + 1], height[r]) * (r - l - 1)
            # new_right = min(height[l], height[r - 1]) * (r - l - 1)
            # if new_left >= new_right:
            #     l += 1
            #     max_area = max(max_area, new_left)
            # else:
            #     r -= 1
            #     max_area = max(max_area, new_right)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            max_area = max(max_area, min(height[l], height[r]) * (r - l))

        return max_area
