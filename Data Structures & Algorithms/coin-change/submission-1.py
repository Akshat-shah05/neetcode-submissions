class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        q = deque([(amount, 0)])
        seen = set([amount])

        while q:
            remaining, coinsSoFar = q.popleft()
            if remaining == 0:
                return coinsSoFar
            
            for coin in coins:
                subAmount = remaining - coin
                if subAmount >= 0 and subAmount not in seen:
                    q.append((subAmount, coinsSoFar + 1))
                    seen.add(subAmount)
        
        return -1
        

        