class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqList = [[] for _ in range(len(nums) + 1)]
        freqMap = defaultdict(int)

        for i in nums:
            freqMap[i] += 1
        
        for num, freq in freqMap.items():
            freqList[freq].append(num)
        
        ans = []
        for i in range(len(freqList) - 1, -1, -1):
            for num in freqList[i]:
                ans.append(num)
                k -= 1
                if k == 0:
                    return ans
            

        return ans