from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # can use dfs to detect cycle
        graph = defaultdict(list)
        for prereq in prerequisites:
            graph[prereq[0]].append(prereq[1])

        visited = defaultdict(int) # 0 unvisited, 1 visiting, 2 visted already

        def dfs(c): # return True if cycle, False otherwise
            if visited[c]==1:
                return True
            if visited[c]==2:
                return False

            visited[c] = 1
            for nei in graph[c]:
                if dfs(nei):
                    return True

            visited[c] = 2
            return False

            
        for i in range(numCourses):
            if graph[i] and visited[i]==0:
                if dfs(i):
                    return False

        return True
        

        