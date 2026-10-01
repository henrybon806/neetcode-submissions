class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.indegree = [0] * numCourses
        self.indegreeList = [[] for _ in range(numCourses)]
        self.visited = []
        self.queue = []

        for i in range(len(prerequisites)):
            self.indegree[prerequisites[i][0]] += 1
            self.indegreeList[prerequisites[i][1]].append(prerequisites[i][0])

        def explore():
            while self.queue:
                cur = self.queue.pop(0)
                self.visited.append(cur)
                for course in self.indegreeList[cur]:
                    self.indegree[course] -= 1
                    if self.indegree[course] == 0:
                        self.queue.append(course)
        
        for i in range(numCourses):
            if self.indegree[i] == 0:
                self.queue.append(i)
        
        explore()

        if len(self.visited) == numCourses:
            return self.visited
        return []
