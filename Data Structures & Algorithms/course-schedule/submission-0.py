class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        can use DFS to detect cycles.
        build neighbors graph first. then iterate through numcourses.
        keep track of what we are visiting in current dfs, if we 
        detect a node that we are still visiting in current traversal,
        return False to detect cycle. if we dont, just return true
        check dfs(i) for all nodes i 
        '''
        dependencies = {i:[] for i in range(numCourses)}
        for pre in prerequisites:
            dependencies[pre[1]].append(pre[0])

        visiting = set()
        def dfs(c): # return False if cycle detected
            if c in visiting:
                return False
            if len(dependencies[c]) == 0:
                return True # no dependencies to check
        
            visiting.add(c)
            for course in dependencies[c]:
                if not dfs(course):
                    return False

            visiting.remove(c)
            return True
            

        for i in range(numCourses):
            if i in dependencies:
                if not dfs(i):
                    return False

        return True
