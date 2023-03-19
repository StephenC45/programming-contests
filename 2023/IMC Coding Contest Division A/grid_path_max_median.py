"""
An attempt at the Grid Path Max Median problem from the 2023 IMC x CSESoc x 
CPMSoc Coding Competition Advanced Division.

This solution was written by my teammate.

This passed both sample test cases but failed all 6 other test cases due to 
a runtime error.
"""



N = int(input())

count = 0
gridArr = []
rowArr = []

while (count < N):
    rowArr = []
    rowInput = input()
    rowArr = rowInput.split(" ")
    rowArr = [ int(x) for x in rowArr ]
    gridArr.append(rowArr)
    count += 1

# code
class Solution:
     
    def __init__(self):
        self.mapping = {}
     
    def printAllPaths(self, M, m, n):
        if not self.mapping.get((m,n)):
            if m == 1 and n == 1:
                return [M[m-1][n-1]]
            else:
                res = []
                if n > 1:
                    a = self.printAllPaths(M, m, n-1)
                    for i in a:
                        if not isinstance(i, list):
                            i = [i]
                        res.append(i+[M[m-1][n-1]])
                if m > 1:
                    b = self.printAllPaths(M, m-1, n)
                    for i in b:
                        if not isinstance(i, list):
                            i = [i]
                        res.append(i+[M[m-1][n-1]])
            self.mapping[(m,n)] = res
        return self.mapping.get((m,n))
 
a = Solution()
res = a.printAllPaths(gridArr, N, N)

largestMedian = 0

for i in res:
    currArray = sorted(i)

    if (currArray[N] > largestMedian):
        largestMedian = currArray[N-1]

print(largestMedian)
