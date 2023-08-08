class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []
        d = {}

        for s in strs:
            letters = ''.join(sorted([*s]))
            if letters not in d:
                d[letters] = len(d)

            if len(groups) <= d[letters]:
                groups.append([])
            groups[d[letters]].append(s)

        return groups
