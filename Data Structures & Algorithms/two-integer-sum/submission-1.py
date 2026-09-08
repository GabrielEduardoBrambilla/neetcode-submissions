class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i in range(len(nums)):
            missing = target - nums[i]
            if missing in hm:
                return [hm[missing], i]
            else:
                hm[nums[i]] = i