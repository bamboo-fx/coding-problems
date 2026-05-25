class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # start at ends and enclose, don't add to new array

        l, r = 0, len(arr) - 1

        # iterate until window is equal to k

        while r - l + 1 > k:
            if abs(x - arr[l]) <= abs(x - arr[r]):
                r -= 1
            else:
                l += 1

        return arr[l:r+1]