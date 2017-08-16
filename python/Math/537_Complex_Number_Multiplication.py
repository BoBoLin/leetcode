'''
Given two strings representing two complex numbers.

You need to return a string representing their multiplication. Note i2 = -1 according to the definition.

Example 1:
Input: "1+1i", "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
Example 2:
Input: "1+-1i", "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.

Note:
The input strings will not have extra blank.
The input strings will be given in the form of a+bi,
where the integer a and b will both belong to the range of [-100, 100].
And the output should be also in this form.
'''


class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        get = lambda s : list(map(int, s[:-1].split('+')))
        a1, a2 = get(a)
        b1, b2 = get(b)
        r = str( a1 * b1 - a2 * b2 )
        i = str( a1 * b2 + a2 * b1 )
        return r + "+" + i + "i"

if __name__ == "__main__":
	
	a = "1+1i"
	b = "1+1i"

	result = Solution().complexNumberMultiply(a, b)
	print (result)