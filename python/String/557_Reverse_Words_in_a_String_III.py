'''
Given a string,
you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.

Difficulty : Easy

'''
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []

        for word in s.split(): # split 
        	result.append(word[::-1])

        return " ".join(result)

if __name__ == "__main__":
	s = "Let's take LeetCode contest"
	
	result = Solution().reverseWords(s)
	print (result)