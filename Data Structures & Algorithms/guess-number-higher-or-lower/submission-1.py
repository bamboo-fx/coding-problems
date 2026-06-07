# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        """
        We can solve with binary search at every point call guess, then
        move left or right based on value
        """
        l, r = 0, n
        while l <= r:
            middle = (l+r) // 2
            result = guess(middle)
            if result == 0:
                return middle
            elif result == -1:
                r = middle - 1
            else:
                l = middle + 1
        return l