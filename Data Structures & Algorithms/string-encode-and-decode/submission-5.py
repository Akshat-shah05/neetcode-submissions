class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += str(len(string)) + ":" + string
        
        return encoded

    def decode(self, s: str) -> List[str]:
        l, r = 0, 0
        ans = []

        while l < len(s):
            while s[r] != ":":
                r += 1
            num = int(s[l : r])
            l = r + 1
            r += (num + 1)
            ans.append(s[l : r])
            l = r
        
        return ans



