class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        lenAns = 0
        for i in range(len(s)):
            # Even Length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > lenAns:
                    ans = s[l : r + 1]
                    lenAns = r - l + 1
                l -= 1
                r += 1

            # Odd Length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > lenAns:
                    ans = s[l : r + 1]
                    lenAns = r - l + 1
                l -= 1
                r += 1
        
        return ans