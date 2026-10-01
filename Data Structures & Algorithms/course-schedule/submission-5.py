class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.indegree = [0] * numCourses
        self.indegreeList = [[] for _ in range(numCourses)]
        self.queue = []
        self.visited = set()
        self.order = []

        for i in prerequisites:
            if i[0] == i[1]:
                return False
            self.indegree[i[0]] += 1
            self.indegreeList[i[1]].append(i[0])

        def explore():
            while self.queue:
                curr = self.queue.pop(0)
                self.visited.add(curr)
                for req in self.indegreeList[curr]:
                    self.indegree[req] -= 1
                    if self.indegree[req] == 0:
                        self.queue.append(req)
            
        for i in range(numCourses):
            if self.indegree[i] == 0:
                self.queue.append(i)
        explore()
        return len(self.visited) == numCourses

        

