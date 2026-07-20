class Solution:

    def encode(self, strs: List[str]) -> str:
        result=""
        for w in strs:
            result +=str(len(w))+"#"+w
        return result

    def decode(self, s: str) -> List[str]:
        arr, l = [], 0
     
        while l < len(s):
            r = l

            while s[r] != "#":
                r +=1 
            lenght = int(s[l : r])
            arr.append(s[r+1 : r + 1 + lenght])
            l = r+1+lenght
        return arr