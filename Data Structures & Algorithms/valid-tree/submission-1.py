class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        adj = defaultdict(list)

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()

        def dfs(node):
            if node in visited:
                return 
            
            visited.add(node)

            for child in adj[node]:
                dfs(child)

        dfs(0)
        return len(visited) == n


        