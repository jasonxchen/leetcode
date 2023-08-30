class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_set = set()
        max_length = 0
        l = 0

        for i, letter in enumerate(s):
            while letter in s_set:
                s_set.remove(s[l])
                l += 1
            s_set.add(letter)
            max_length = max(max_length, i - l + 1)

        return max_length
