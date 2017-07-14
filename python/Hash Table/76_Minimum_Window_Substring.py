'''
Given a string S and a string T,
find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.

Difficulty: Hard

'''

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        cur_cnt = [0 for i in xrange(58)]
        fin_cnt = [0 for i in xrange(58)]
        
        for each_t_char in t :
        	fin_cnt[ord(each_t_char) - ord('A')] += 1

        i, match, front = 0, 0, 0
        min_width, min_start = float("inf"), 0
        while i < len(s) :
        	pos = ord(s[i]) - ord('A')
        	cur_cnt[pos] += 1
        	if cur_cnt[pos] <= fin_cnt[pos]:
        		match += 1

        	if match == len(t):
        		while fin_cnt[ord(s[front]) - ord('A')] == 0 or cur_cnt[ord(s[front]) - ord('A')] > fin_cnt[ord(s[front]) - ord('A')] :
        			cur_cnt[ord(s[front]) - ord('A')] -= 1
        			front += 1
        		if min_width > i - front + 1 :
        			min_width = i - front + 1
        			min_start = front
        	i += 1

        if min_width == float('inf'):
        	return ""

        return s[min_start: min_start + min_width]


if __name__ == "__main__":
	s = "ADOBECODEBANC"
	t = "ABC"
	result = Solution().minWindow(s, t)
	print result
