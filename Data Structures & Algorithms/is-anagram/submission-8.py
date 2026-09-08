class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm1 = {}
        hm2 = {}
        if len(s) != len(t):
            return False

        for char in s:
            if char in hm1:
                hm1[char] += 1
            else:
                hm1[char] = 1

        
        for char in t:
            if char in hm2:
                hm2[char] += 1
            else:
                hm2[char] = 1

        return hm1 == hm2