class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area, l, r = 0, 0, len(heights) - 1

        while l < r:
            newArea = (r - l) * min(heights[l], heights[r])
            area = max(area, newArea)

            if heights[l] <= heights[r]:
                l += 1
            
            else:
                r -= 1
        
        return area
        