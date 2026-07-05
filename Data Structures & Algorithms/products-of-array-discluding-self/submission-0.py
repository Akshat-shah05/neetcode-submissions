class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # make prefix and postfix products arrays
        # For each index, multiply prefix till that index by postfix after that index
        n = len(nums)
        prefix, postfix = [1] * n, [1] * n
        prefix[0], postfix[-1] = nums[0], nums[-1]

        for i in range(1, n):
            prefix[i] = nums[i] * prefix[i - 1]
        
        for i in range(n - 2, -1, -1):
            postfix[i] = nums[i] * postfix[i + 1]
        
        ans = [1] * n
        ans[0] = postfix[1]
        ans[-1] = prefix[-2]

        for i in range(1, n - 1):
            ans[i] = prefix[i - 1] * postfix[i + 1]
        
        return ans
            

        