class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # two pointers
        # start at the ends and increment inwards
        l, r = 0, len(arr) - 1
        # until len(res) = k or r - l < k (something like that)

        # while r - l <= k
        # return the window of arr
        while r - l + 1 > k:
            if abs(x - arr[l]) <= abs(x - arr[r]):
                r -= 1
            else:
                l += 1
        return arr[l:r+1]