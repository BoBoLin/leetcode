'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Difficulty:Medium

'''
#捷徑問題

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        m -= 1
        n -= 1
        return Solution().factorial(m + n) / (Solution().factorial(m) * Solution().factorial(n))


    def factorial(self, n):
    	if(n <= 1):
    		return 1
    	else :
    		return Solution().factorial(n-1) * n


if __name__ == "__main__":
	m = 3
	n = 7

	result = Solution().uniquePaths(m, n)
	print (result)
	#print (Solution().factorial(3))