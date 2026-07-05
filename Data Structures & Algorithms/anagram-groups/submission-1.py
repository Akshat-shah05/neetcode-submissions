class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for string in strs:
            # keep track of count in an array
            count = [0] * 26
            for char in string:
                count[ord('a') - ord(char)] += 1
            
            ans[tuple(count)].append(string)
        
        return ans.values()