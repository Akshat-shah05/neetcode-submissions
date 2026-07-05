class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}

        for a, b in prerequisites:
            adj[a].append(b)

        visiting = set()
        
        def dfs(course):
            if course in visiting:
                return False
            
            if adj[course] == []:
                return True
            
            visiting.add(course)
            for child in adj[course]:
                if not dfs(child):
                    return False
            visiting.remove(course)
            adj[course] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
        