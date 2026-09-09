class Solution:
    def countCommas(self, n: int) -> int:
        total = 0
        thr = 1000

        while thr <= n:
            total += n - thr + 1
            thr *= 1000

        return total
        
    
        