#In MATLAB, there is a very useful function called 'reshape',
#which can reshape a matrix into a new one with different size but keep its original data.

#You're given a matrix represented by a two-dimensional array,
#and two positive integers r and c representing the row number and column number
#of the wanted reshaped matrix, respectively.

#The reshaped matrix need to be filled with all the elements of the original matrix
#in the same row-traversing order as they were.

#If the 'reshape' operation with given parameters is possible and legal,
#output the new reshaped matrix; Otherwise, output the original matrix.
'''
Example 1:
Input: 
nums = [[1,2],
	    [3,4]]
r = 1, c = 4
Output: 
[[1,2,3,4]]
Explanation:
The row-traversing of nums is [1,2,3,4].
The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.
Example 2:
Input: 
nums = 
[[1,2],
 [3,4]]
r = 2, c = 4
Output: 
[[1,2],
 [3,4]]
Explanation:
There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.

Note:
The height and width of the given matrix is in range [1, 100].
The given r and c are all positive.
'''
#Difficulty: Easy

#####  solution 1
'''
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums) * len(nums[0]) != r*c:
        	return nums
        
        result = [[None for column in range(c)] for row in range(r)]
        row_count, col_count = 0, 0

        for row_set in nums:
        	for each_element in row_set:
        		print each_element
        		result[row_count][col_count] = each_element
        		col_count += 1
        		if col_count == c :
        			col_count = 0
        			row_count += 1

        return result

if __name__ == "__main__":
	test_list = [[1,2],[3,4]]
	r, c = 1, 4
	result = Solution().matrixReshape(test_list, r, c)
	print result
'''
####  !solution 1

####  solution 2
import numpy as np
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums) * len(nums[0]) != r * c:
        	return nums

        return np.reshape(nums, (r, c)).tolist()  #array to list

sol = Solution()
nums = [[1,2],[3,4],[5,6]]
print sol.matrixReshape(nums, 2, 3)

####  !solution 2