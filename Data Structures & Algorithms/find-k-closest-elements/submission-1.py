class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, 0
        abs_min = float("INF")
        min_arr = []
        full_array = []
        local_min = 0
        while r < len(arr):
            if (r - l + 1) == k:
                for i in range(l,r+1):
                    local_min += abs(x - arr[i])
                    min_arr.append(arr[i])           
                if local_min < abs_min:
                    abs_min = local_min
                    full_array.append(min_arr)
                r += 1
                l += 1
                local_min = 0
                min_arr = []
            else:
                r += 1
        return full_array[-1]