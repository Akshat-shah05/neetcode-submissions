class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            newString = str(len(string)) + "#" + string
            encoded += newString
        
        return encoded
        
    def decode(self, s: str) -> List[str]:
        ans = []

        i = 0
        while i < len(s):
            num = ""
            word = ""
            while s[i] != "#":
                num += s[i]
                i += 1
            i += 1
            wordLength = int(num)
            for j in range(i, i + wordLength):
                word += s[j]
            
            i = i + wordLength
            ans.append(word)
        
        return ans

            

            