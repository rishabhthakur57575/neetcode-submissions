class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        all_product = 1
        without_zero_product = 1
        zero_count = 0
        res = []

        for i in nums:
            all_product *= i
            if i == 0:
                zero_count += 1
                continue
            else: without_zero_product *= i

        for i in nums:
            if i == 0:
                res.append(without_zero_product if zero_count == 1 else 0)
            else:
                res.append(int(all_product/i))
            
        return res