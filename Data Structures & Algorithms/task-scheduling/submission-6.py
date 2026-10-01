class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        count = Counter(tasks)
        heap = [(-c, task) for task, c in count.items()]
        heapq.heapify(heap)

        cooldown = []
        time = 0

        while heap or cooldown:
            still_cooling = []
            for i in range(len(cooldown)):
                if cooldown[i][1] <= time:
                    if cooldown[i][0][0] < 0:
                        heapq.heappush(heap, cooldown[i][0])
                else:
                    still_cooling.append(cooldown[i])
            cooldown = still_cooling
            if heap:
                cnt, task = heapq.heappop(heap)
                cnt += 1
                if cnt < 0:
                    cooldown.append(((cnt,task), time+n+1))
                time += 1
            elif cooldown:
                time = min(t for (_,t) in cooldown)

        return time
