class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        counts = {s[r]: 1}
        max_count = 1
        max_count_curr = True
        max_length = 1

        while r < len(s):
            if r - l + 1 - max_count - k <= 0:
                max_length = max(max_length, r - l + 1)
                r += 1
                if r < len(s):
                    counts[s[r]] = counts.get(s[r], 0) + 1
                    if counts[s[r]] > max_count:
                        max_count = counts[s[r]]
                        max_count_curr = True
            else:
                if counts[s[l]] == max_count_curr:
                    max_count_curr = False
                counts[s[l]] -= 1
                l += 1

        return max_length
