class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        results = []
        for n in range(numRows):
            row = [1]
            C = 1
            for k in range(1, n + 1):
                C = C * (n - k + 1) // k
                row.append(C)
            results.append(row)
        return results 
