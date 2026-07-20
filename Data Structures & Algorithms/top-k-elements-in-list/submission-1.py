class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        bucket = [[] for num in range(len(nums)+1)]
        value= []
        for num in nums:
            if num in hashmap:
                hashmap[num] = hashmap[num] + 1
            else:
                hashmap[num] = 1
       
        for keys in hashmap:
            bucket[hashmap[keys]].append(keys) 
        
        for num in nums:
            value.extend(bucket.pop())
            print(bucket)
            print(value)
            if len(value) >= k:
                return value
                
