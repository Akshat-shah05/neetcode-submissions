class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProduct = nums[:]
        postfixProduct = nums[:]
        n = len(nums)

        for i in range(1, n):
            prefixProduct[i] = prefixProduct[i] * prefixProduct[i - 1]
        
        for i in range(n - 2, -1, -1):
            postfixProduct[i] = postfixProduct[i] * postfixProduct[i + 1]
        
        output = []
        for i in range(n):
            if i == 0:
                output.append(postfixProduct[1])
            
            elif i == n - 1:
                output.append(prefixProduct[n - 2])
            
            else:
                output.append(prefixProduct[i - 1] * postfixProduct[i + 1])
        
        return output

