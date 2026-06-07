class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        I think what we have to do is perform a binary search to get the
        correct row and then within the row do the correct column and then
        return True or False if we find a match or not
        
        Perform a binary search on the first number in the rows, in each
        given row perform a binary search on the columns?
        """
        # filter for potential row in which target is located

        top, bottom = 0, len(matrix) - 1

        # binary search to see potential row
        while top <= bottom:
            row = (top+bottom) // 2
            if matrix[row][0] > target:
                bottom = row - 1
            elif matrix[row][-1] < target:
                top = row + 1
            else:
                break
        
        # filters for exact row where either we find interval in row where target fits ie matrix[row][0] <= target <= matrix[row][-1]
        # or we found no possible rows so quick check:
        if not (top <= bottom):
            return False
        
        # get the actual possible row (doesn't save from while loop not scoped)
        row = (top+bottom) // 2
        l, r = 0, len(matrix[0]) - 1
        # normal binary search on given row to iterate through columns to find target
        while l <= r:
            middle = (l+r) // 2
            if matrix[row][middle] == target:
                return True
            elif matrix[row][middle] < target:
                l = middle + 1
            else:
                r = middle - 1
        return False
