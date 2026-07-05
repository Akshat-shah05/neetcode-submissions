class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = defaultdict(int)
        for num in nums:
            freqMap[num] += 1
        
        buckets = [[] for _ in range(len(nums) + 1)]
        for key, val in freqMap.items():
            buckets[val].append(key)

        ans = []
        
        for i in range(len(buckets) - 1, -1, -1):
            bucket = buckets[i]
            for val in bucket:
                ans.append(val)
                k -= 1
                if k == 0:
                    return ans

        return ans
