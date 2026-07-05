class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for string in strs:
            encoded += str(len(string)) + "#" + string
        
        return encoded
 
    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            num = 0
            while s[i] != "#":
                num = num * 10 + int(s[i])
                i += 1
                    
            ans.append(s[i + 1 : i + num + 1])
            i = i + num + 1

        return ans

