class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        memo = {}
        def dp(remaining):
            if remaining < 0:
                return -1
            
            if remaining == 0:
                return 0
            
            if remaining in memo:
                return memo[remaining]
            
            best = float('inf')
            for coin in coins:
                res = dp(remaining - coin)
                if res != -1:
                    best = min(best, res + 1)
            
            memo[remaining] = best
            return memo[remaining]
        
        ans = dp(amount)
        return ans if ans != float('inf') else -1

        