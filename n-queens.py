# ans = []

# def dfs(cur, n):
#     if len(cur) == n:
#         ans.append(cur)
#         return cur
    
    
#     for row in range(n):
#         if can_place(cur, row):
#             dfs(cur + [row], n)

#     return ans

# def can_place(cur, x):
#     for i, y in enumerate(cur):
#         if y == x or len(cur) - i == abs(x - y):
#             return False
    
#     return True

# print(dfs([], 8))

# https://leetcode.com/problems/n-queens/description/
class Solution:
    def __init__(self):
        self.res = []

    
    def solveNQueens(self, n):
        return self.dfs([], n)

    def dfs(self, cur, n):
        if len(cur) == n:
            cur = ["."* i + "Q" + "."*(len(cur) - i - 1) for i in cur]
            self.res.append(cur)
            return cur

        for row in range(n):
            if self.can_place(cur, row):
                self.dfs(cur + [row], n)

        return self.res

    def can_place(self, cur, x):
        for i, y in enumerate(cur):
            if y == x or len(cur) - i == abs(x - y):
                return False

        return True

a = Solution()
print(a.solveNQueens(8))

