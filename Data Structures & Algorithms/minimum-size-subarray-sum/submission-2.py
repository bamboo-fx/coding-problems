class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        small_len = 0
        min_counter = float("INF")
        l = 0
        for r in range(len(nums)):
            small_len += nums[r]
            if small_len >= target:
                min_counter = min(min_counter, r - l + 1)
                while small_len >= target and l <= r:
                    min_counter = min(min_counter, r - l + 1)
                    small_len -= nums[l]
                    l += 1

        return 0 if min_counter == float("INF") else min_counter