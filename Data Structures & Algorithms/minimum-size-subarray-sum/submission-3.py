class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        l = 0
        min_array = float("INF")
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                min_array = min(min_array, r - l + 1)
                total -= nums[l]
                l += 1

            
        return min_array if min_array != float("INF") else 0