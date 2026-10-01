class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = set()

        for i in range(len(nums)):
            seen = set()
            for j in range(i+1, len(nums)):
                if j == i:
                    continue
                if -(nums[i] + nums[j]) in seen:
                    curr = sorted([nums[i],nums[j],-(nums[i] + nums[j])])
                    output.add(tuple(curr))
                seen.add(nums[j])

        return [[x[0],x[1],x[2]] for x in output]
