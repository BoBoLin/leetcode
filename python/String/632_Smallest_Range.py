'''
You have k lists of sorted integers in ascending order.
Find the smallest range that includes at least one number from each of the k lists.

We define the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c if b-a == d-c.

Example 1:
Input:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
Output: [20,24]
Explanation: 
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].
Note:
The given list may contain duplicates, so ascending order means >= here.
1 <= k <= 3500
-105 <= value of elements <= 105.
For Java users, please note that the input type has been changed to List<List<Integer>>.
And after you reset the code template, you'll see this point.

Difficulty : Hard

'''

import collections

class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """

        dic = collections.defaultdict(set)
        cover = collections.defaultdict(set)

        for index, each_list in enumerate(nums):
        	for num in each_list :
        		dic[num].add(index)

        total = sorted(set(n for nlist in nums for n in nlist))
        total_size = len(total)
        start, end = 0, 0
        result = [total[0], total[-1]]  #先設最大區間
        diff = float("inf")

        while start < total_size and end < total_size :
        	while end < total_size and len(cover) < len(nums) :
        		for index in dic[total[end]] :
        			cover[index].add(total[end])
        		end += 1

        	while start < total_size and len(cover) == len(nums) :
        		if total[end - 1] - total[start] < diff and len(cover) == len(nums) :
        			diff = total[end - 1] - total[start]
        			result = [total[start], total[end - 1]]
        		for index in dic[total[start]] :
        			cover[index].remove(total[start])
        			if len(cover[index]) == 0 :
        				del cover[index]
        		start += 1

        return result


if __name__ == "__main__":
	nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
	
	result = Solution().smallestRange(nums)
	print (result)


