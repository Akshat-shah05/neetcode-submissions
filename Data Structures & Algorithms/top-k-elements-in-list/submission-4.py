class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freqArr = [[] for _ in range(n + 1)]
        countMap = defaultdict(int)
        for num in nums:
            countMap[num] += 1
        
        for key, value in countMap.items():
            freqArr[value].append(key)

        ans = []
        for i in range(n, -1, -1):
            for num in freqArr[i]:
                ans.append(num)
                k -= 1
                if k == 0:
                    return ans
        
        return ans


