class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freqDict = defaultdict(int)
        freqArray = [[] for _ in range(n + 1)]

        for i in nums:
            freqDict[i] += 1

        for key, val in freqDict.items():
            freqArray[val].append(key)

        ans = []
        for i in range(n, -1, -1):
            for j in freqArray[i]:
                ans.append(j)
                k -= 1
                if k == 0:
                    return ans
