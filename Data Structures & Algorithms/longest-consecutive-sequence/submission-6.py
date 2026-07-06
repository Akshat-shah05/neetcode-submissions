class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
            
        numSet = set(nums)
        longest = 1
        current = 1

        for num in nums:
            if num - 1 in numSet:
                continue
            
            x = num + 1
            while x in numSet:
                current += 1
                x += 1
            
            longest = max(longest, current)
            current = 1
        
        return longest
