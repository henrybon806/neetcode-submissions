class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        count = Counter(p for row in wall for p in accumulate(row[:-1]))
        return len(wall) - max(count.values(), default=0)