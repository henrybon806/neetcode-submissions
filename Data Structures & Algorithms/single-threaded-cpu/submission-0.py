class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:    
        res = []
        sorted_tasks = deque(sorted([(x[0], x[1], i) for i, x in enumerate(tasks)]))
        pstart, ptime, plabel = sorted_tasks.popleft()
        queue = [(ptime, plabel)] #priority queue
        curr = pstart
        while queue:
            time, label = heapq.heappop(queue)
            res.append(label)
            curr += time
            
            while sorted_tasks and sorted_tasks[0][0] <= curr:
                pstart, ptime, plabel = sorted_tasks.popleft()
                heapq.heappush(queue, (ptime, plabel))
            if not queue and sorted_tasks:
                pstart, ptime, plabel = sorted_tasks.popleft()
                heapq.heappush(queue, (ptime, plabel))
                curr = pstart
                
        return res
