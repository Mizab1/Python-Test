class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i is not j:
                    return [i, j]

sol = Solution()
result = sol.twoSum([3,2,4], 6)
print(result)