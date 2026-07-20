class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, num in enumerate(numbers):
            t = target - num
            if t in hashmap:
                return [ hashmap[t] +1, i+1]
            else: 
                hashmap[num] = i