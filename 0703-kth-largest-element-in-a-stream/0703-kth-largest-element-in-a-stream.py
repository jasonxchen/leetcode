class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)

        while len(self.nums) > k:
            self.nums.pop(0)

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            self.nums.append(val)
            self.nums = sorted(self.nums)
        elif val > self.nums[0]:
            self.nums[0] = val
            self.nums = sorted(self.nums)

        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)