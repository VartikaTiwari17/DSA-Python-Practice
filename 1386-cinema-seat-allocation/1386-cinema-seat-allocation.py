class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        
        row_mask = defaultdict(int)
        for r, s in reservedSeats:
            row_mask[r] |= (1 << s)
        
        LEFT   = 0b0000111100   # seats 2,3,4,5
        MIDDLE = 0b0011110000   # seats 4,5,6,7
        RIGHT  = 0b1111000000   # seats 6,7,8,9
        
        # rows with no reservations at all -> 2 groups each
        total = (n - len(row_mask)) * 2
        
        for mask in row_mask.values():
            if (mask & LEFT) == 0 and (mask & RIGHT) == 0:
                total += 2
            elif (mask & LEFT) == 0 or (mask & MIDDLE) == 0 or (mask & RIGHT) == 0:
                total += 1
        
        return total