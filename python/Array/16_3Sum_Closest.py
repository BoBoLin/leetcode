#Given an array S of n integers,
#find three integers in S such that the sum is closest to a given number, target.
#Return the sum of the three integers.
#You may assume that each input would have exactly one solution.

#For example, given array S = {-1 2 1 -4}, and target = 1.
#The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        min_diff = float('Inf') 
        i = 0
        
       	while i < len(nums) - 2 :
       		if (i == 0) or (nums[i] != nums[i-1]):
       			j = i + 1
       			k = len(nums) - 1
       			while j < k :
       				diff = nums[i] + nums[j] + nums[k] - target
       				if abs(diff) < min_diff:
       					min_diff = abs(diff)
       					result = nums[i] + nums[j] + nums[k]
       				if diff > 0 :
       					k = k - 1
       				elif diff < 0 :
       					j = j + 1
       				else : # diff == 0
       					return target
       		i = i + 1

       	return result

if __name__ == "__main__":
	result = Solution().threeSumClosest([-1, 2, 1, -4], 1)
	#result = Solution().threeSumClosest([1,2, 2, 3, -4, -10], 1)
	print result


        
        