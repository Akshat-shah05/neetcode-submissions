class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, num in enumerate(nums):
            if num > 0:
                break  # every subsequent number is larger so theres no point
            
            if i > 0 and num == nums[i - 1]:
                continue  # we already found all possibilities for that start don't repeat
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = num + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1
                
                elif threeSum < 0:
                    l += 1
                
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
            
        return res
        