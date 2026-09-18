class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {}

        for i in range(len(nums)):
            numsMap[nums[i]] = i

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numsMap and i != numsMap[complement]:
                return [i, numsMap[complement]]

        return []
        