class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        postfix = [1] * n
        prefix[0], postfix[-1] = nums[0], nums[-1]

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i]
        
        for i in range(n - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i]
        
        ans = [1] * n
        ans[0] = postfix[1]
        ans[-1] = prefix[-2]
        for i in range(1, n - 1):
            ans[i] = postfix[i + 1] * prefix[i - 1]
        
        return ans