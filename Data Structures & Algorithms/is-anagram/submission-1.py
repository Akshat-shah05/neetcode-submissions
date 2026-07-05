class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmap1 = defaultdict(int)
        hmap2 = defaultdict(int)

        for char in s:
            hmap1[char] += 1
        
        for char in t:
            hmap2[char] += 1
        
        return hmap1 == hmap2