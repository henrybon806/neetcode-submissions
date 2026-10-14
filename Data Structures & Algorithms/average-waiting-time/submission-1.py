class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        totalwait = 0
        prev = 0
        for arrival, time in customers:
            rollover = max(prev-arrival, 0)
            totalwait += time + rollover
            prev = arrival+time+rollover
        
        return totalwait / len(customers)