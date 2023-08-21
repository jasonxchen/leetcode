class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        s_array = [*s]
        max_length = 0

        for i, letter in enumerate(s_array):
            d = {letter: 1}
            length = 1

            for j in range(i + 1, len(s)):

                if s_array[j] in d:
                    break
                else:
                    d[s_array[j]] = 1
                    length += 1

            max_length = max(max_length, length)

        return max_length
