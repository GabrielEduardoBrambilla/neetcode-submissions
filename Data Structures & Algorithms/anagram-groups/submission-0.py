class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)
        for s in strs:
            alph = [0] * 26
            for c in s:
                alph[ord(c) - ord('a')] += 1
            hm[tuple(alph)].append(s)
        return list(hm.values())