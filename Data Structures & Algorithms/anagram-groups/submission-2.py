class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)

        for string in strs:
            charArr = [0] * 26
            for char in string:
                charArr[ord(char) - ord('a')] += 1
            
            hmap[tuple(charArr)].append(string)
        
        return list(hmap.values())