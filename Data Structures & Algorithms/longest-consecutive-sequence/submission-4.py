class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        numset = set(nums)
        longest = 1

        for num in nums:
            if num - 1 in numset:
                continue
            
            x = num
            count = 1
            while x + 1 in numset:
                x += 1
                count += 1

            longest = max(longest, count)

        return longest 