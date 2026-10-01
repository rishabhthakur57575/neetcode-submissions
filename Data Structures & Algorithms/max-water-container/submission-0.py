class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        i = 0
        j = len(heights) - 1

        while i < j:
            length = j - i
            temp = 0

            if heights[i] > heights[j]:
                temp = heights[j] * length
                j -= 1
            else:
                temp = heights[i] * length
                i += 1

            result = temp if temp > result else result

        return result
