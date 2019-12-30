#http://ouwang.me/2019/01/20/Python-LeetCode-70-Climbing-Stairs/
class Solution(object):
    cache = {}    
    def climbStairs(self, n):
        if n < 3:
            return n
        else:
            return self._climbStairs(n-1) + self._climbStairs(n-2)
    def _climbStairs(self, n):
        if n not in self.cache.keys():
            self.cache[n] = self.climbStairs(n)
        return self.cache[n]
