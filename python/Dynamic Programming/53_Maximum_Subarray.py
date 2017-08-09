'''
Find the contiguous subarray within an array (containing at least one number)
which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
More practice:
If you have figured out the O(n) solution,
try coding another solution using the divide and conquer approach, which is more subtle.

Difficulty : Easy

'''
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if max(nums) < 0 :
        	return max(nums)
        total_max = float('-inf')
        tmp_max = 0
        start, end, count = 0, 0, 0 
        for x in nums :
        	if tmp_max == 0 and x >= 0:
        		start = count

        	tmp_max = max(0, tmp_max + x)

        	if tmp_max >= total_max :
        		total_max = tmp_max
        		end = count

        	#total_max = max(total_max, tmp_max)

        	count += 1
        #print "start", start
        #print "end", end
        sublist = nums[start:end+1]
        return total_max, sublist

if __name__ == "__main__":
	nums = [-2,1,-3,4,-1,2,1,-5,4]

	result, sublist = Solution().maxSubArray(nums)
	print (result, sublist)