class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # cache = [[0 for _ in range(n)] for _ in range (m)]
        # return self.dfsHelper(0, 0, m, n, cache)
        prevRow = [0] * n

        for r in range(m - 1, -1, -1):
            currRow = [0] * n
            currRow[n-1] = 1
            for c in range(n-2, -1, -1):
                currRow[c] = currRow[c+1] + prevRow[c]
            prevRow = currRow
        return prevRow[0]

    # def dfsHelper(self, r, c, rows, cols, cache):
    #     # base case : out of bounds 
    #     if r == rows or c == cols: 
    #         return 0

    #     # base case : reach destination
    #     if r == rows - 1 or c == cols - 1:
    #         return 1

    #     # cache hit
    #     if cache[r][c] > 0:
    #         return cache[r][c]
        
    #     # Reccursive case
    #     cache[r][c] =  self.dfsHelper(r+1, c, rows, cols, cache) + self.dfsHelper(r, c+1, rows, cols, cache)
    #     return cache[r][c]