class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        sort = []
        for num in counts:
            sort.append((counts[num], num))
        sort.sort()
        return [x[1] for x in sort][len(sort)-k:]
