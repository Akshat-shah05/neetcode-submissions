class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setOfNums = set(nums)

        longest = 0

        for i in nums:
            if i - 1 not in nums:
                curr = 1

                while curr + i in setOfNums:
                    curr += 1
                
                longest = max(longest, curr)
        
        return longest
        