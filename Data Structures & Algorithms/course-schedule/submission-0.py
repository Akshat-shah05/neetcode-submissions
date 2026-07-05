class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        cycleMap = {}

        for a, b in prerequisites:
            adj[a].append(b)
        
        def dfs(course):
            if course in cycleMap:
                return cycleMap[course]
            
            cycleMap[course] = False

            for child in adj[course]:
                if not dfs(child):
                    return False
            
            cycleMap[course] = True
            return cycleMap[course]
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
        