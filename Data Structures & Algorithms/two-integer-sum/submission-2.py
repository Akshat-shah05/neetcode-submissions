class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in hmap:
                return [hmap[needed], i]
            
            hmap[nums[i]] = i
        