class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        counts = {}
        max_count = 0
        max_length = 0

        for r in range(len(s)):
            counts[s[r]] = counts.get(s[r], 0) + 1
            max_count = max(max_count, counts[s[r]])
            if r - l + 1 - max_count - k <= 0:
                max_length = max(max_length, r - l + 1)
            else:
                counts[s[l]] -= 1
                l += 1

        return max_length
