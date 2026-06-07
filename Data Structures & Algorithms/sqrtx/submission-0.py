class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l <= r:
            middle = (l+r) // 2
            if middle * middle == x:
                return middle
            elif middle * middle < x:
                l = middle + 1
            else:
                r = middle - 1
        return r