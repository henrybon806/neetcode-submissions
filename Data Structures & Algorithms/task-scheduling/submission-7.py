class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        count = Counter(tasks)
        heap = [-c for c in count.values()]
        heapq.heapify(heap)

        cooldown = deque()
        time = 0

        while heap or cooldown:
            if cooldown and cooldown[0][1] <= time:
                heapq.heappush(heap, cooldown.popleft()[0])
            
            if heap:
                cnt = heapq.heappop(heap)
                cnt += 1
                if cnt < 0:
                    cooldown.append((cnt, time+n+1))
                time += 1
            elif cooldown:
                time = min(t for (_,t) in cooldown)

        return time
