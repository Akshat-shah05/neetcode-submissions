class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmap1 = defaultdict(int)
        hmap2 = defaultdict(int)

        for i in s:
            hmap1[i] += 1
        
        for i in t:
            hmap2[i] += 1
        
        return hmap1 == hmap2
        