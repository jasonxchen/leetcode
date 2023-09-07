class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        counts = {s[r]: 1}
        max_length = 0

        while r < len(s):
            if r - l + 1 - counts[max(counts, key=counts.get)] - k <= 0:
                max_length = max(max_length, r - l + 1)
                r += 1
                if r < len(s):
                    counts[s[r]] = counts.get(s[r], 0) + 1
            else:
                counts[s[l]] -= 1
                l += 1

        # for l in range(len(s)):
        #     counts = {s[l]: 1}
        #     for r in range(l + 1, len(s)):
        #         counts[s[r]] = counts.get(s[r], 0) + 1
        #         if r - l + 1 - counts[max(counts, key=counts.get)] - k <= 0:
        #             max_length = max(max_length, r - l + 1)

        return max_length
